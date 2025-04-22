import pandas as pd
import os,subprocess,sys
from datetime import datetime, timedelta
from collections import Counter

def get_call_file_path():
    from VersionDATA.ai_renderer import call_file_path
    return call_file_path.Call()

call = get_call_file_path()

class Infer_time_model():
    def extract_training_data_with_dates(self,file_path):
        try:
            df = pd.read_csv(file_path)
            df.columns = df.columns.str.strip()

            result = []
            for _, row in df.iterrows():
                date = row['date'] if 'date' in row and pd.notna(row['date']) else 0
                sentence = row['sentence']
                sent_type = row['sentence_type']
                intent = row['intent']
                result.append((date, sent_type, intent, sentence))

            return result
        except Exception as e:
            print(f"Error extracting training data: {e}")
            return []

    def count_sentences_per_day_with_details(self,result):
        filtered = [r for r in result if r[0] != 0]

        def parse_date_flexibly(date_str):
            for fmt in ("%Y-%m-%d %H:%M:%S", "%d/%m/%Y %H:%M", "%Y-%m-%d", "%d/%m/%Y"):
                try:
                    return datetime.strptime(date_str, fmt).date()
                except ValueError:
                    continue
            raise ValueError(f"Unknown date format: {date_str}")


        date_sentences = {}

        for r in filtered:
            date = parse_date_flexibly(r[0])
            sentence_details = {"sentence": r[3], "sentence_type": r[1], "intent": r[2]}

            if date not in date_sentences:
                date_sentences[date] = []

            date_sentences[date].append(sentence_details)

        return date_sentences

    def calculate_average_type_and_intent_per_day(self,daily_sentences):
        daily_avg_types_and_intents = {}

        # Iterate over each day and calculate the average types and intents
        for date, sentences in daily_sentences.items():
            type_counter = Counter()
            intent_counter = Counter()

            # Count occurrences of types and intents for each day
            for sentence in sentences:
                type_counter[sentence['sentence_type']] += 1
                intent_counter[sentence['intent']] += 1

            # Calculate average types and intents for the day
            total_sentences = len(sentences)
            avg_types = {key: count / total_sentences for key, count in type_counter.items()}
            avg_intents = {key: count / total_sentences for key, count in intent_counter.items()}

            # Store the result for this day
            daily_avg_types_and_intents[date] = {
                "average_types": avg_types,
                "average_intents": avg_intents
            }

        return daily_avg_types_and_intents

    def find_dates_with_minimum_overture(self,daily_avg_types_and_intents,days):
        # Sort the dates in chronological order
        sorted_dates = sorted(daily_avg_types_and_intents.keys())

        # Find pairs of dates with a minimum 5-day separation
        date_pairs = []
        for i in range(len(sorted_dates) - 1):
            date1 = sorted_dates[i]
            date2 = sorted_dates[i + 1]

            # Check if the dates are at least 5 days apart
            if (date2 - date1).days >= int(days):
                date_pairs.append((date1, date2))

        return date_pairs

    def calculate_change_in_types_and_intents(self,daily_avg_types_and_intents, date_pairs):
        change_details = []

        # Iterate over each pair of dates
        for date1, date2 in date_pairs:
            # Get the average types and intents for both dates
            types_day1 = daily_avg_types_and_intents[date1]["average_types"]
            types_day2 = daily_avg_types_and_intents[date2]["average_types"]

            intents_day1 = daily_avg_types_and_intents[date1]["average_intents"]
            intents_day2 = daily_avg_types_and_intents[date2]["average_intents"]

            # Calculate the change in types and intents
            type_changes = {}
            intent_changes = {}

            # Calculate changes for sentence types
            for sent_type in types_day1:
                change = types_day2.get(sent_type, 0) - types_day1.get(sent_type, 0)
                type_changes[sent_type] = change

            # Calculate changes for intents
            for intent in intents_day1:
                change = intents_day2.get(intent, 0) - intents_day1.get(intent, 0)
                intent_changes[intent] = change

            change_details.append({
                "date1": date1,
                "date2": date2,
                "type_changes": type_changes,
                "intent_changes": intent_changes
            })

        return change_details


def run_model(days,days_ago_to_show):
    file_path_path_versionDATA_name_sentences = call.versionDATA_trainingdata_sentences()
    infer_time_model = Infer_time_model()
    result = infer_time_model.extract_training_data_with_dates(file_path_path_versionDATA_name_sentences)
    daily_details = infer_time_model.count_sentences_per_day_with_details(result)
    avg_types_and_intents_per_day = infer_time_model.calculate_average_type_and_intent_per_day(daily_details)
    date_pairs = infer_time_model.find_dates_with_minimum_overture(avg_types_and_intents_per_day,days)
    change_in_types_and_intents = infer_time_model.calculate_change_in_types_and_intents(avg_types_and_intents_per_day, date_pairs)
    days_ago = datetime.now().date() - timedelta(days=int(days_ago_to_show))
    recent_changes = [
        change for change in change_in_types_and_intents
        if change["date2"] >= days_ago
    ]
    def get_changes_summary(change_in_types_and_intents):
        summary = []

        for change in change_in_types_and_intents:
            type_changes_str = ", ".join([f"{sent_type}: {change_val:.2f}" for sent_type, change_val in change["type_changes"].items()])
            intent_changes_str = ", ".join([f"{intent}: {change_val:.2f}" for intent, change_val in change["intent_changes"].items()])

            summary.append(f"Sentence Changes from {change['date1']} to {change['date2']}:")
            summary.append(f"  Type Changes: {type_changes_str}")
            summary.append(f"  Intent Changes: {intent_changes_str}")

        return "\n".join(summary)

    changes_summary = get_changes_summary(recent_changes)
    return changes_summary

#run_model(5,5) ##make this configurable in settings



