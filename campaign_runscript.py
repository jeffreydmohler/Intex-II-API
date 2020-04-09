import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'intexapi.settings'
import django
django.setup()
from api.models import Campaign, Update, Donation
import json

def main():
    # read the json data
    with open('campaign.json', encoding='ascii', errors='ignore') as json_data:
        data = json.load(json_data)
    for camp in data['campaigndata']:
        c = Campaign()
        c.id = camp['id']
        c.url = camp['url']
        c.campaign_id = camp['campaign_id']
        c.auto_fb_post_mode = camp['auto_fb_post_mode']
        c.collected_date = camp['collected_date']
        c.category_id = camp['category_id']
        c.currencycode = camp['currencycode']
        c.current_amount = camp['current_amount']
        c.goal = camp['goal']
        c.donators = camp['donators']
        c.days_active = camp['days_active']
        c.days_created = camp['days_created']
        c.title = camp['title']
        c.description = camp['description']
        c.default_url = camp['default_url']
        c.has_beneficiary = camp['has_beneficiary']
        c.media_type = camp['media_type']
        c.project_type = camp['project_type']
        c.turn_off_donations = camp['turn_off_donations']
        c.user_id = camp['user_id']
        c.user_first_name = camp['user_first_name']
        c.user_last_name = camp['user_last_name']
        c.user_profile_url = camp['user_profile_url']
        c.visible_in_search = camp['visible_in_search']
        c.status = camp['status']
        c.deactivated = camp['deactivated']
        c.state = camp['state']
        c.is_launched = camp['is_launched']
        c.campaign_image_url = camp['campaign_image_url']
        c.created_at = camp['created_at']
        c.launch_date = camp['launch_date']
        c.campaign_hearts = camp['campaign_hearts']
        c.social_share_total = camp['social_share_total']
        c.social_share_last_update = camp['social_share_last_update']
        c.location_city = camp['location_city']
        c.location_country = camp['location_country']
        c.location_zip = camp['location_zip']
        c.is_charity = camp['is_charity']
        c.charity_valid = camp['charity_valid']
        c.charity_npo_id = camp['charity_npo_id']
        c.charity_name = camp['charity_name']
        c.velocity = camp['velocity']
        c.location_state = camp['location_state']
        c.current_amount_USD = camp['current_amount_USD']
        c.goal_USD = camp['goal_USD']
        c.percent_of_goal = camp['percent_of_goal']
        c.amount_per_donation = camp['amount_per_donation']
        c.percent_of_goal_score = camp['percent_of_goal_score']
        c.amt_per_donor_score = camp['amt_per_donor_score']
        c.success_score = camp['success_score']
        c.save()   
if __name__ == '__main__':
    main()
