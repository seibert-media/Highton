Highton
===========

##Highton is a python library for Highrise
Install via Pip:

    pip install highton

Thank you that you came to my repository. Feel free to work with my API. - Bykof
##What you can do with Highton?

 * You can get/put/post/delete nearly all Highrise-data (working on it!)
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
    print(person.first_name)

#or get all deals since a datetime for a faster import
#Format is YYYYMMDDHHMMSS
deals = high.get_deals_since('20140601000000')

for deal in deals:
    print(deal.name)

"""
    Set the current authenticated
    account on the Highton instance.
"""
high.set_account()
print(high.account)
#enjoy your output

```
#Highton Functions

##Account

Never a bad idea to set the account context on the Highton instance.

    high.get_account()
    # Set the currently authenticated account as a member of the class. Can access the account with `high.account`.

Or yourself;

    high.get_current_auth_user()
    # Set the currently authenticated user as a member of the instance. Can access yourself with `high.me`

##GET

Get all users

    cases = high.get_users()

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

Get Notes from a Person/Company/Case/Deal

    notes = high.get_person_notes('person_highrise_id')
    notes = high.get_company_notes('company_highrise_id')
    notes = high.get_case_notes('case_highrise_id')
    notes = high.get_deal_notes('deal_highrise_id')

#All of the above also have a single getter.

Get a {case/company/contact/...} like that

    thing = high.get_{case/company/contact/...}(str(HIGHRIGE_ID))

Get a case like that

    case = high.get_case(HIGHRIGE_ID)

Get Deleted items

    dele = high.get_deleted()

Get deleted items since

    dele = high.get_deleted_since('YYYYMMDDHHmmss')

##POST
  * data: You must (for now) use an xml string for the request data. There will soon be a way to send dicts or tuples.
    sample_xml = "<{TYPE}><{KEY}>Refer to the basecamp docs</{KEY}></{TYPE}>"

Create a case

    high.post_case(data)

Create a company

    high.post_company(data)

Create a custom_field

    high.post_custom_field(data)

Create a deal

    high.post_deal(data)

Create a email

    high.post_email(data)

Create a subject_email with a subject type and subject id

    high.post_subject_email(subject_type, subject_id, data)

Create a note

    high.post_note(data)

Create a subject_note with a subject type and subject id

    high.post_subject_note(subject_type, subject_id, data)

Create a person

    high.post_note(data)

Create a task

    high.post_task(data)

##UPDATE
  * data: You must (for now) use an xml string for the request data. There will soon be a way to send dicts or tuples.
    sample_xml = "<{TYPE}><{KEY}>Refer to the basecamp docs</{KEY}></{TYPE}>"

  * Pass {'reload': 'true'} if you want to use the successfully updated item. If you pass {'reload': 'true'} then you will get back a dict: `{'request': request, 'model', HightonModel}` else ignore the param to get back just the response.

Update a case

    high.put_case(highrise_id, data, {params})

Update a company

    high.put_company(highrise_id, data, {params})

Update a custom_field

    high.put_custom_field(highrise_id, data, {params})

Update a deal

    high.put_deal(highrise_id, data, {params})

Update a email

    high.put_email(highrise_id, data, {params})

Update a note

    high.put_note(highrise_id, data, {params})

Update a person

    high.put_note(highrise_id, data, {params})

Update a task

    high.put_task(highrise_id, data, {params})

##DESTROY

  * Simply send in the Highrise ID
  * Only the response is returned for now since this is a lightweight uselesss table.

Destroy a case

    high.delete_case(highrise_id, data, {params})

Destroy a comment

    high.delete_comment(highrise_id, data, {params})

Destroy a company

    high.delete_company(highrise_id, data, {params})

Destroy a custom_field

    high.delete_custom_field(highrise_id, data, {params})

Destroy a deal

    high.delete_deal(highrise_id, data, {params})

Destroy an email

    high.delete_email(highrise_id, data, {params})

Destroy a group

    high.delete_group(highrise_id, data, {params})

Destroy a note

    high.delete_note(highrise_id, data, {params})

Destroy a person

    high.delete_note(highrise_id, data, {params})

Destroy a task

    high.delete_task(highrise_id, data, {params})

#Classes

##Highton
 * account (After calling high.get_account())
  * highrise_id
  * created_at
  * updated_at
  * name
  * plan
  * subdomain
  * color_theme
  * ssl_enabled
  * people_count
  * storage
 * me (After calling high.get_current_auth_user())
  * name
  * subdomain
  * plan
  * color_theme
  * ssl_enabled
  * people_count
  * storage

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

##Notes
 * highrise_id
 * body
 * author_id
 * subject_id
 * subject_type
 * subject_name
 * collection_id
 * collection_type
 * visible_to
 * owner_id
 * group_id
 * updated_at
 * created_at
 * attachments

##Attachment
 * highrise_id
 * url
 * name
 * size

##Deletion
 * highrise_id
 * type
 * deleted_at

##User
 * highrise_id
 * name
 * email_address
 * created_at
 * updated_at
 * admin
