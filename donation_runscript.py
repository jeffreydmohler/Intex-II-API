import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'intexapi.settings'
import django
django.setup()
from api.models import Campaign, Update, Donation
import json

def main():
    # read the json data
    with open('donation.json', encoding='ascii', errors='ignore') as json_data:
        data = json.load(json_data)
    for don in data['donationdata']:
        d = Donation()
        d.id = don['id']
        d.campaign_id = don['campaign_id']
        d.collected_date = don['collected_date']
        d.amount = don['amount']
        d.is_offline = don['is_offline']
        d.is_anonymous = don['is_anonymous']
        d.name = don['name']
        d.created_at = don['created_at']
        d.profile_url = don['profile_url']
        d.verified = don['verified']
        d.save()   
if __name__ == '__main__':
    main()
