import os
import requests

SUPABASE_URL = "https://znljnvxlunewgqdneqto.supabase.co"
SERVICE_ROLE_KEY = "sb_secret_QE7eymh_5gSxyS1EKDdafg_zweGnKsr"
BUCKET_NAME = "files"

# അപ്‌ലോഡ് ചെയ്യേണ്ട ഫോൾഡർ പാത്ത് (ഇവിടെ പ്രൊജക്റ്റ് ഡയറക്ടറിയാണ് എടുക്കുന്നത്)
TARGET_DIR = "/home/hacker/workspace"  # നിങ്ങളുടെ ആവശ്യാനുസരണം മാറ്റാം

def get_existing_files():
    """Supabase-ൽ നിലവിലുള്ള ഫയലുകളുടെ ലിസ്റ്റ് എടുക്കുന്നു"""
    url = f"{SUPABASE_URL}/storage/v1/object/list/{BUCKET_NAME}"
    clean_key = SERVICE_ROLE_KEY.strip()
    headers = {
        "Authorization": f"Bearer {clean_key}",
        "apikey": clean_key,
        "Content-Type": "application/json"
    }
    # റീകർസീവ് ആയി ഫയലുകൾ ലിസ്റ്റ് ചെയ്യാൻ ബോഡി നൽകാം
    response = requests.post(url, json={"prefix": ""}, headers=headers)
    if response.status_code == 200:
        return [item['name'] for item in response.json()]
    return []

def upload_all_files():
    clean_key = SERVICE_ROLE_KEY.strip()
    existing_files = get_existing_files()
    
    # ഫോൾഡറിലെ മുഴുവൻ ഫയലുകളും പരിശോധിക്കുന്നു
    for root, dirs, files in os.walk(TARGET_DIR):
        # .git പോലുള്ള അനാവശ്യ സിസ്റ്റം ഫോൾഡറുകൾ ഒഴിവാക്കാൻ
        if '.git' in root:
            continue
            
        for file in files:
            file_path = os.path.join(root, file)
            file_name = os.path.relpath(file_path, TARGET_DIR)
            
            # ഫയൽ ഇതിനകം ഡാറ്റാബേസിൽ ഉണ്ടോ എന്ന് പരിശോധിക്കുന്നു
            if file_name in existing_files:
                continue  # ഉണ്ടെങ്കിൽ വീണ്ടും അപ്‌ലോഡ് ചെയ്യില്ല
                
            url = f"{SUPABASE_URL}/storage/v1/object/{BUCKET_NAME}/{file_name}"
            
            with open(file_path, 'rb') as f:
                headers = {
                    "Authorization": f"Bearer {clean_key}",
                    "apikey": clean_key
                }
                response = requests.post(url, data=f, headers=headers)
                
            if response.status_code == 200:
                print(f"Uploaded: {file_name}")
            else:
                print(f"Failed: {file_name} ({response.status_code})")

if __name__ == "__main__":
    upload_all_files()
