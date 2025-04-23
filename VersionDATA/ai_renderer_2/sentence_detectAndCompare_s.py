import pandas as pd
import os, subprocess, sys
from datetime import datetime, timedelta,date
from collections import Counter
import random

def get_call_file_path():
    from VersionDATA.ai_renderer import call_file_path
    return call_file_path.Call()

call = get_call_file_path()

class Infer_time_model:
    def extract_training_data_with_dates(self, file_path):
        try:
            df = pd.read_csv(file_path)
            df.columns = df.columns.str.strip()
            result = []
            for _, row in df.iterrows():
                date_val = row.get('date', None)
                date_str = date_val if pd.notna(date_val) else None
                sentence = row.get('sentence', '')
                sent_type = row.get('sentence_type', '')
                intent = row.get('intent', '')
                result.append((date_str, sent_type, intent, sentence))
            return result
        except Exception as e:
            print(f"Error extracting training data: {e}")
            return []

    def count_sentences_with_details(self, data, granularity='day'):
        def parse_date(s):
            if not s:
                return None
            for fmt in ("%Y-%m-%d %H:%M:%S", "%d/%m/%Y %H:%M", "%Y-%m-%d", "%d/%m/%Y"):
                try:
                    return datetime.strptime(s, fmt).date()
                except Exception:
                    continue
            raise ValueError(f"Unknown date format: {s}")

        grouped = {}
        for date_str, stype, intent, text in data:
            d = parse_date(date_str)
            if d is None:
                continue
            if granularity == 'week':
                d = d - timedelta(days=d.weekday())
            elif granularity == 'month':
                d = d.replace(day=1)
            elif granularity == 'year':
                d = d.replace(month=1, day=1)
            # else 'day' uses full date
            grouped.setdefault(d, []).append({'sentence_type': stype, 'intent': intent, 'sentence': text})
        return grouped

    def calculate_average_type_and_intent(self, grouped):
        averages = {}
        for key, items in grouped.items():
            type_ctr = Counter()
            intent_ctr = Counter()
            total = len(items)
            for itm in items:
                type_ctr[itm['sentence_type']] += 1
                intent_ctr[itm['intent']] += 1
            averages[key] = {
                'average_types': {k: v/total for k, v in type_ctr.items()},
                'average_intents': {k: v/total for k, v in intent_ctr.items()}
            }
        return averages

    def find_date_pairs(self, averages, min_gap):
        keys = sorted(averages.keys())
        pairs = []
        for i in range(len(keys)-1):
            if (keys[i+1] - keys[i]).days >= int(min_gap):
                pairs.append((keys[i], keys[i+1]))
        return pairs

    def calculate_change_in_types_and_intents(self, averages, pairs):
        changes = []
        for d1, d2 in pairs:
            t1 = averages.get(d1, {}).get('average_types', {})
            t2 = averages.get(d2, {}).get('average_types', {})
            i1 = averages.get(d1, {}).get('average_intents', {})
            i2 = averages.get(d2, {}).get('average_intents', {})
            type_changes = {k: t2.get(k,0) - t1.get(k,0) for k in t1}
            intent_changes = {k: i2.get(k,0) - i1.get(k,0) for k in i1}
            changes.append({'period1': d1, 'period2': d2, 'type_changes': type_changes, 'intent_changes': intent_changes})
        return changes

    def summarize_changes(self, changes):
        lines = []
        for c in changes:
            types = ', '.join(f"{k}: {v:.2f}" for k,v in c['type_changes'].items())
            intents = ', '.join(f"{k}: {v:.2f}" for k,v in c['intent_changes'].items())
            lines.append(f"Changes from {c['period1']} to {c['period2']}:\n  Type Changes: {types}\n  Intent Changes: {intents}")
        return '\n'.join(lines)

def run_model(past_d_changes, changes_d_apart_at_leastDays, granularity='day'):
    model = Infer_time_model()
    data = model.extract_training_data_with_dates(call.versionDATA_trainingdata_sentences())
    grouped = model.count_sentences_with_details(data, granularity)
    averages = model.calculate_average_type_and_intent(grouped)
    pairs = model.find_date_pairs(averages, past_d_changes)
    changes = model.calculate_change_in_types_and_intents(averages, pairs)
    cutoff = datetime.now().date() - timedelta(days=int(changes_d_apart_at_leastDays))

    recent = []
    for c in changes:
        # Ensure d2 is a date (already is one in this case)
        d2 = c['period2']
        if d2 >= cutoff:
            recent.append(c)

    if not recent and changes:
        recent = [changes[-1]]

    return model.summarize_changes(recent)

# Example:
# run_model(5, 5, granularity="week")

