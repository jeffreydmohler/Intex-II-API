import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'intexapi.settings'
import django
django.setup()
from api.models import Campaign, Update, Donation
import json

def main():
    # read the json data
    with open('update.json', encoding='ascii', errors='ignore') as json_data:
        data = json.load(json_data)
    for upd in data['updatedata']:
        u = Update()
        u.id = upd['id']
        u.campaign_id = upd['campaign_id']
        u.collected_date = upd['collected_date']
        u.photo_url = upd['photo_url']
        u.created_at = upd['created_at']
        u.updates_author = upd['updates_author']
        u.updates_author_type = upd['updates_author_type']
        u.updates_text = upd['updates_text']
        u.save()   
if __name__ == '__main__':
    main()
