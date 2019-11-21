test_str = {
    'contacts':
[
    {'phoneNumbers': [{'label': 'mobile', 'number': '010-3499-2882', 'id': '9223372034707292162'}, {'label': 'mobile', 'number': '010-8515-6285', 'id': '9223372034707292163'}], 'rawContactId': '9223372034707292161', 'jobTitle': '', 'givenName': '준희', 'company': '', 'hasThumbnail': False, 'prefix': None, 'recordID': '9223372034707292161', 'displayName': '원준희', 'postalAddresses': [], 'middleName': None, 'emailAddresses': [], 'familyName': '원', 'urlAddresses': [], 'thumbnailPath': '', 'department': '', 'suffix': None, 'note': ''},
     {'phoneNumbers': [{'label': 'mobile', 'number': '01026146124', 'id': '20'}], 'rawContactId': '3', 'jobTitle': '', 'givenName': '개망나니', 'company': '', 'hasThumbnail': False, 'prefix': None, 'recordID': '6', 'displayName': '개망나니', 'postalAddresses': [], 'middleName': None, 'emailAddresses': [], 'familyName': None, 'urlAddresses': [], 'thumbnailPath': '', 'department': '', 'suffix': None, 'note': ''},
     {'phoneNumbers': [{'label': 'mobile', 'number': '010-3451-3838', 'id': '34'}, {'label': 'mobile', 'number': '01031373236', 'id': '35'}], 'rawContactId': '5', 'jobTitle': '', 'givenName': '류재', 'company': '', 'hasThumbnail':False, 'prefix': None, 'recordID': '351', 'displayName': '류재', 'postalAddresses': [], 'middleName': None, 'emailAddresses': [], 'familyName': None, 'urlAddresses': [], 'thumbnailPath': '', 'department': '', 'suffix': None, 'note': ''},
     {'phoneNumbers': [{'label': 'work', 'number': '010-8558-2880', 'id': '42'}, {'label': 'mobile', 'number': '01195582880', 'id': '43'}, {'label': 'work', 'number': '010-8558-2880', 'id': '1917'}, {'label': 'mobile', 'number': '011-9558-2880', 'id': '1918'}], 'rawContactId': '599', 'jobTitle': '', 'givenName': '아부지', 'company': '', 'hasThumbnail': False, 'prefix': '', 'recordID': '671', 'displayName': '아부지', 'postalAddresses': [], 'middleName': '', 'emailAddresses': [], 'familyName': '', 'urlAddresses': [], 'thumbnailPath': '', 'department': '', 'suffix': '', 'note': ''},
   ]
 }
contacts = ''
print(type(data_dict['contacts']))
for a in data_dict['contacts']:
    print(a['displayName'])
    print(a['note'])
    for b in a['phoneNumbers']:
        print(b['number'])



ffff = {'contacts': [{'givenName': '준희', 'rawContactId': '9223372034707292161',
                      'phoneNumbers': [{'label': 'mobile', 'number': '010-3499-2882', 'id': '9223372034707292162'}, {'label': 'mobile', 'number': '010-8515-6285', 'id': '9223372034707292163'}], 'note': '', 'department': '', 'thumbnailPath': '', 'jobTitle': '', 'company': '', 'suffix': None, 'displayName': '원준희', 'recordID': '9223372034707292161', 'postalAddresses': [], 'hasThumbnail': False, 'familyName': '원', 'middleName': None, 'urlAddresses': [], 'emailAddresses': [], 'prefix': None}, {'givenName': '개망나니', 'rawContactId': '3',
                        'phoneNumbers': [{'label': 'mobile', 'number': '01026146124', 'id': '20'}], 'note': '', 'department': '', 'thumbnailPath': '', 'jobTitle': '', 'company': '', 'suffix': None, 'displayName': '개망나니', 'recordID': '6', 'postalAddresses': [], 'hasThumbnail': False, 'familyName': None, 'middleName': None, 'urlAddresses': [], 'emailAddresses': [], 'prefix': None}, {'givenName': '류재', 'rawContactId': '5',
'phoneNumbers': [{'label': 'mobile', 'number': '010-3451-3838', 'id': '34'}, {'label': 'mobile', 'number': '01031373236', 'id': '35'}], 'note': '', 'department': '', 'thumbnailPath': '', 'jobTitle': '', 'company': '', 'suffix': None, 'displayName': '류재', 'recordID': '351', 'postalAddresses': [], 'hasThumbnail': False, 'familyName': None, 'middleName': None, 'urlAddresses': [], 'emailAddresses': [], 'prefix': None}, {'givenName': '아부지', 'rawContactId': '599',
'phoneNumbers': [{'label': 'work', 'number': '010-8558-2880', 'id': '42'}, {'label': 'mobile', 'number': '01195582880', 'id': '43'}, {'label': 'work', 'number': '010-8558-2880', 'id': '1917'}, {'label': 'mobile', 'number': '011-9558-2880', 'id': '1918'}], 'note': '', 'department': '', 'thumbnailPath': '', 'jobTitle': '', 'company': '', 'suffix': '', 'displayName': '아부지', 'recordID': '671', 'postalAddresses': [], 'hasThumbnail': False, 'familyName': '', 'middleName': '', 'urlAddresses': [], 'emailAddresses': [], 'prefix': ''}, {'givenName': '초난감', 'rawContactId': '598',
'phoneNumbers': [{'label': 'work', 'number': '010-7377-4450', 'id': '50'}, {'label': 'mobile', 'number': '01033010851', 'id': '51'}, {'label': 'work', 'number': '010-7377-4450', 'id': '1914'}, {'label': 'mobile', 'number': '010-3301-0851', 'id': '1915'}], 'note': '', 'department': '', 'thumbnailPath': '', 'jobTitle': '', 'company': '', 'suffix': '', 'displayName': '초난감', 'recordID': '18', 'postalAddresses': [], 'hasThumbnail': False, 'familyName': '', 'middleName': '', 'urlAddresses': [], 'emailAddresses': [], 'prefix': ''}, {'givenName': '우리집', 'rawContactId': '8',
'phoneNumbers': [{'label': 'mobile', 'number': '0513382882', 'id': '58'}], 'note': '', 'department': '', 'thumbnailPath': '', 'jobTitle': '', 'company': '', 'suffix': None, 'displayName': '우리집', 'recordID': '1', 'postalAddresses': [], 'hasThumbnail': False, 'familyName': None, 'middleName': None, 'urlAddresses': [], 'emailAddresses': [], 'prefix': None}, {'givenName': '성차이햄', 'rawContactId': '9',
'phoneNumbers': [{'label': 'mobile', 'number': '01030046378', 'id': '65'}], 'note': '', 'department': '', 'thumbnailPath': '', 'jobTitle': '', 'company': '', 'suffix': None, 'displayName': '성차이햄', 'recordID': '12', 'postalAddresses': [], 'hasThumbnail': False, 'familyName': None, 'middleName': None, 'urlAddresses': [], 'emailAddresses': [], 'prefix': None}, {'givenName': '준용이', 'rawContactId': '11',
'phoneNumbers': [{'label': 'mobile', 'number': '01050313520', 'id': '79'}], 'note': '', 'department': '', 'thumbnailPath': '', 'jobTitle': '', 'company': '', 'suffix': None, 'displayName': '준용이', 'recordID': '2', 'postalAddresses': [], 'hasThumbnail': False, 'familyName': None, 'middleName': None, 'urlAddresses': [], 'emailAddresses': [], 'prefix': None}, {'givenName': '현', 'rawContactId': '12',}]}

print(type(ffff))



CREATE TABLE `con_table` (

  `id` bigint(20) unsigned NOT NULL auto_increment,
  `name` varchar(255) ,

    `phone` varchar(255),
`memo` varchar(255) ,
`insertdate` datetime,
PRIMARY KEY (`id`)

) ENGINE=InnoDB DEFAULT CHARSET=euckr;



[mysqld]

default-character-set=utf8
default-collation=utf8_general_ci



CREATE TABLE `LADDER_INFO` (

    `DATE` varchar(20) NOT NULL ,
    `COUNT` varchar(255) NOT NULL,
    `TIME` varchar(255),
    `START_POINT` varchar(255),
    `LINE` varchar(255),
    `RESULT` varchar(255),
    `insertdate` datetime,

PRIMARY KEY (`DATE`,`COUNT`)

) ENGINE=InnoDB DEFAULT CHARSET=euckr;





def insert_ladder(DATE,COUNT,TIME,START_POINT,LINE,RESULT):
    db = pymysql.connect(host=config.DATABASE_CONFIG_LADDER['host'], port=config.DATABASE_CONFIG_LADDER['port'], user=config.DATABASE_CONFIG_LADDER['user'], passwd=config.DATABASE_CONFIG_LADDER['password'], db=config.DATABASE_CONFIG_LADDER['dbname'], charset=config.DATABASE_CONFIG_LADDER['charset'])
    curs = db.cursor()
    sql = """insert into LADDER_INFO(DATE,COUNT,TIME,START_POINT,LINE,RESULT) values(%s,%s,%s,NOW())"""
    curs.execute(sql,(DATE,COUNT,TIME,START_POINT,LINE,RESULT))
    # print(URI)
    db.commit()
    db.close()
