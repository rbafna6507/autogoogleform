import requests
from datetime import date

today = date.today()

bruh_url = "https://docs.google.com/forms/d/1ipjkccPwZUBAnA4nQkZg2jJ0q97XZ49sZ7MwJMfAIvE/formResponse"
calc_url = 'https://docs.google.com/forms/d/e/1FAIpQLScSHXQt8lBZoKyMjkvhMWNi7I0WfOO3ay3c8n3Qro-YJ_0giw/formResponse'
compsci_url = 'https://docs.google.com/forms/d/1FAIpQLSeLbRcBtMidmKYN01g_D6LeK4RyX1bftJSABGmViJe9yzdxOg/formResponse'
psych_url = 'https://docs.google.com/forms/d/1FAIpQLSdpIiX1PE_EQxv_ThJ0TBXBoTXlB_faom4g5nQfPSpHVdp49Q/formResponse'
lang_url = 'https://docs.google.com/forms/d/e/1FAIpQLSc_OSSqv5afDf7Za-OIRgyZEO5w-veCR-zaebuwJeOu_o9jPQ/formResponse'
bro_subs = {"entry.297025561": "Rohan Bafna"}
calc_subs = {"entry.616020434": "Bafna", "entry.570950898": "Rohan", "entry.816737777": "7 AP AB Virtual", "entry.2110622356": "I am a Virtual Student"}
compsci_subs = {"entry.616020434": "Bafna", "entry.570950898": "Rohan", "entry.816737777": "7 AP Computer Science Virtual", "entry.2110622356": "I am a Virtual Student"}
psych_subs = {"entry.340679026": "Bafna, Rohan"}
lang_subs = {"entry.616020434": "Bafna", "entry.570950898": "Rohan", "entry.2110622356": "I am a Virtual Student", "entry.816737777": "4 AP Language"}
requests.post(calc_url, calc_subs)
requests.post(compsci_url, compsci_subs)
requests.post(psych_url, psych_subs)
requests.post(lang_url, lang_subs)
requests.post(bruh_url, bro_subs)
print('attendance marked at ', today)
