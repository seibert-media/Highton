Highton
===========

##Highton is a python library for Highrise
Install via Pip:

    pip install highton

Thank you that you came to my repository. Feel free to work with my API. - Bykof
##What you can do with Highton?

 * You can get nearly all Highrise-data (working on it!)
 * Every data you get from Highton is structured in a simple class - structure (more a the bottom)
 * You have a lot of exception-handler in there so don't worry about to fail
 * Yeah Highton means Highrise and Python - you got it!


##How does the Highton API work?
You will have the main class so just import Highton to your libraries and call some functions:

```python
#import Highton
from highton import Highton

#initialize it
high = Highton(
    api_key = 'xxxxxxxxxxxxxxxxxxxxxxxxx',
    user = 'company_name_or_account'
)

"""
    now you can use every method
    example: 
    yes it will iterate over all pages
    not only the first 500
"""
people = high.get_people()

#iterate over all people
for person in people:
#choose one of the attributes from below
    print person.first_name
    
#or get all deals since a datetime for a faster import
#Format is YYYYMMDDHHMMSS
deals = high.get_deals_since('20140601000000')

for deal in deals:
    print deal.name
#enjoy your output
```
#Highton Functions

Get all cases

    cases = high.get_cases()

Get cases since dateimte
    
    cases_since_datetime = high.get_cases_since('YYYMMDDHHMMSS')
    
Get people
    
    people = high.get_people()
    
Get people since datetime

    people = high.get_people_since('YYYMMDDHHMMSS')

Get task categories
    
    task_categories = high.get_task_categories()

Get deal categories
    
    deal_categories = high.get_deal_categories()
    
Get companies

    companies = high.get_companies()

Get companies since datetime

    companies = high.get_companies_since('YYYMMDDHHMMSS')
    
Get deals
    
    deals = high.get_deals()
    
Get deals since datetime
    
    deals = high.get_deals_since('YYYMMDDHHMMSS')
    
Get deals by status
    
    deals = high.get_deals_by_status('status')

Get Tasks from a Person/Company/Case/Deal
    
    tasks = high.get_person_tasks('person_highrise_id')
    tasks = high.get_company_tasks('company_highrise_id')
    tasks = high.get_case_tasks('case_highrise_id')
    tasks = high.get_deal_tasks('deal_highrise_id')



#Classes

##Case
 * highrise_id
 * author_id
 * closed_at
 * created_at
 * updated_at
 * name
 * visible_to
 * group_id
 * owner_id
 * parties

##Category
 * highrise_id,
 * name

###TaskCategory
 * highrise_id
 * name
 * updated_at
 * account_id
 * color
 * created_at
 * elements_count

###DealCategory
 * highrise_id
 * name
 * updated_at
 * account_id
 * color
 * created_at
 * elements_count

##Company
 * highrise_id
 * first_name
 * last_name
 * title
 * background
 * linkedin_url
 * avatar_url
 * company_id
 * company_name
 * created_at
 * updated_at
 * visible_to
 * owner_id
 * group_id
 * author_id
 * phone_numbers
 * email_addresses
 * subject_datas
 * tags

##Contact
 * phone_numbers
 * email_addresses
 * subject_datas
 * tags
 * addresses

###PhoneNumber
 * highrise_id
 * number
 * location

###EmailAdresses
 * highrise_id
 * address
 * location

###Address
 * highrise_id
 * city
 * country
 * location
 * state
 * street

##Person
 * highrise_id
 * first_name
 * last_name
 * title
 * background
 * linkedin_url
 * avatar_url
 * company_id
 * company_name
 * created_at
 * updated_at
 * visible_to
 * owner_id
 * group_id
 * author_id
 * phone_numbers
 * email_addresses
 * subject_datas
 * tags

##Deal
 * account_id
 * author_id
 * background
 * category_id
 * created_at
 * currency
 * duration
 * group_id
 * highrise_id
 * name
 * owner_id
 * party_id
 * price
 * price_type
 * responsible_party_id
 * status
 * status_changed_on
 * updated_at
 * visible_to
 * category
 * party
 * parties

##SubjectData
 * highrise_id
 * value
 * subject_field_id
 * subject_field_label

##Tag
 * highrise_id
 * name

##Task
 * highrise_id
 * subject_id
 * subject_type
 * category_id
 * body
 * frame
 * due_at
 * alert_at
 * created_at
 * author_id
 * updated_at
 * public
 * recording_id
 * subject_id
 * subject_type
 * category_id
 * body
 * frame
 * due_at
 * alert_at
 * created_at
 * author_id
 * updated_at
 * public
