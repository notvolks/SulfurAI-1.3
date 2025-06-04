import SulfurAI
SulfurAI.setup_local()
INPUT_TEXT = SulfurAI.run_locally("GAMARAM FUNK",True)
print(INPUT_TEXT["INPUT_TEXT"][0])
print(INPUT_TEXT["PREDICTED_USER_DEVICE"])
print(INPUT_TEXT["PREDICTED_USER_DEVICE_ACCURACY"])
print(INPUT_TEXT["USER_SENTENCE_INTENT"])
print(INPUT_TEXT["PREDICTED_USER_LOCATION_COUNTRY"])

print(SulfurAI.get_output_data())
print(SulfurAI.get_output_data_ui())
