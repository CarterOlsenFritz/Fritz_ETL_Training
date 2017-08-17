"""
# This block is the raw text.

Sold Offline Conversions

INSERT INTO wheretostay_conversions (e_id, created_date, sold_date, status, commission, gclid, custom_channel, custom_campaign, custom_adgroup, custom_ad)
(56851, 2017-08-05 15:44:58, 2017-08-13, sold, 1207.50, CjwKEAjw--DLBRCN_bW36taJkhwSJABSMEduMhJL-NxfBjy3DIl8Jog9rI4ObCQ-dnG4mXyFJHXpIxoCmxTw_wcB, adwords, 889604337, 44105051505, 208592418140)
(56839, 2017-08-03 20:04:24, 2017-08-14, sold, 1190.00, EAIaIQobChMIsN_p16S81QIVBINpCh1PHQ8EEAAYASAAEgIpO_D_BwE, adwords, 901390551, 43882660934, 211750551501)
Working Offline Conversions

INSERT INTO wheretostay_conversions (e_id, created_date, sold_date, status, commission, gclid, custom_channel, custom_campaign, custom_adgroup, custom_ad)
(56927, 2017-08-14 21:09:58, 0000-00-00, entered, 875.00, CLLo0dvF19UCFcmIswodc7EKZw, adwords, 907860379, 48062788231, 214875939806)
(56926, 2017-08-14 19:17:23, 0000-00-00, entered, 1157.14, Cj0KCQjwlMXMBRC1ARIsAKKGuwj7tLezQpN_8S-8cKfkwj2qO0PO918ZUHE-OV5e4EFusF-rHAofPdwaAt0qEALw_wcB, adwords, 885704867, 43968377506, 207755067488)
(56907, 2017-08-12 15:09:40, 0000-00-00, working, 1015.00, Cj0KCQjwq7XMBRCDARIsAKVI5Qa9JkCO4ux2Uu9YeNJU1AKXz5wtAGGWK4F7-t_3_Y_etHiZPWfASdQaAr32EALw_wcB, adwords, 889604337, 44105048545, 211209447265)
(56911, 2017-08-13 14:52:42, 0000-00-00, working, 3220.00, CjwKCAjwk4vMBRAgEiwA4ftLs4NXIgmpdekwoRHcrb2icpTfoYEN5hcg2P_rHQIce_Qv0y-H_ysgzRoCLy0QAvD_BwE, adwords, 893226458, 40097820850, 208900565262)
(56834, 2017-08-03 10:09:06, 0000-00-00, hot, 771.43, EAIaIQobChMIyZyPi4W71QIV1zyBCh1pXQ2gEAAYAyAAEgJHNvD_BwE, adwords, 895567671, 44798392036, 209511737243)
(56844, 2017-08-04 19:12:35, 0000-00-00, hot, 3571.43, CjwKEAjwtpDMBRC4xebfxpzu8mUSJAA4c-TuNV2H0n3ds9ZVUw5zK9IYzUKkdHV41dM5Oku_oa9VLxoC0W3w_wcB, adwords, 889604337, 44105047185, 208592463809)

I need to remove all of the titles and INSERT INTO lines to just have the VALUES remain. Once we are down to the VALUE lines, manipulate the string into a usable format to then be used in the INSERT INTO statement for the DEV table. If Thom changes the format again then I could possibly skip the title deletion and shit.

Would it be smarter to convert the values into a series of arrays (array of arrays? I don't know the parlance.) So I can do things like on the 4th term (Actually #3), if array[3] == '0000-00-00' then '1901-01-01' and do it for all at once? Fuck if I know right now.


# How the string should be manipulated.
# Find and Replace logic.
1. at every ", " replace with "', '"
2. at every "\(" replace with "\('" -- \ is for escaping
3. at every "\)" replace with "'\)," -- \ is for escaping
4. replace '0000-00-00' with '1901-01-01'
5. Trim the last character (the hanging "," at the end of the string).
"""

# data_raw = string of raw text
# transformations to delete titles and INSERT INTO lines that I don't need so only value lines remain.

# This block is for importing my SQL DB credentials and other packages. I'm not 100% on how packages work here but I'd assume an install to where the python.exe is then 'import' it below here.
#from Credentials import * #import platform credentials and database credentials # use me?
#import csv
#import unicodedata
#import pymssql # use me?
#import glob
#import os
#import datetime # use me?
#import zipfile
#import requests
#import json

#def connect():
#    connection = pymssql.connect(host=HOST,user=USER,password=PASSWORD, database=DATABASE)
#    return connection

data_insert = "test"
print(data_insert)

# Creating a variable that will inherit the trimmed string after the first deletion steps.
data_insert = """(56851, 2017-08-05 15:44:58, 2017-08-13, sold, 1207.50, CjwKEAjw--DLBRCN_bW36taJkhwSJABSMEduMhJL-NxfBjy3DIl8Jog9rI4ObCQ-dnG4mXyFJHXpIxoCmxTw_wcB, adwords, 889604337, 44105051505, 208592418140)
(56839, 2017-08-03 20:04:24, 2017-08-14, sold, 1190.00, EAIaIQobChMIsN_p16S81QIVBINpCh1PHQ8EEAAYASAAEgIpO_D_BwE, adwords, 901390551, 43882660934, 211750551501)
(56927, 2017-08-14 21:09:58, 0000-00-00, entered, 875.00, CLLo0dvF19UCFcmIswodc7EKZw, adwords, 907860379, 48062788231, 214875939806)
(56926, 2017-08-14 19:17:23, 0000-00-00, entered, 1157.14, Cj0KCQjwlMXMBRC1ARIsAKKGuwj7tLezQpN_8S-8cKfkwj2qO0PO918ZUHE-OV5e4EFusF-rHAofPdwaAt0qEALw_wcB, adwords, 885704867, 43968377506, 207755067488)
(56907, 2017-08-12 15:09:40, 0000-00-00, working, 1015.00, Cj0KCQjwq7XMBRCDARIsAKVI5Qa9JkCO4ux2Uu9YeNJU1AKXz5wtAGGWK4F7-t_3_Y_etHiZPWfASdQaAr32EALw_wcB, adwords, 889604337, 44105048545, 211209447265)
(56911, 2017-08-13 14:52:42, 0000-00-00, working, 3220.00, CjwKCAjwk4vMBRAgEiwA4ftLs4NXIgmpdekwoRHcrb2icpTfoYEN5hcg2P_rHQIce_Qv0y-H_ysgzRoCLy0QAvD_BwE, adwords, 893226458, 40097820850, 208900565262)
(56834, 2017-08-03 10:09:06, 0000-00-00, hot, 771.43, EAIaIQobChMIyZyPi4W71QIV1zyBCh1pXQ2gEAAYAyAAEgJHNvD_BwE, adwords, 895567671, 44798392036, 209511737243)
(56844, 2017-08-04 19:12:35, 0000-00-00, hot, 3571.43, CjwKEAjwtpDMBRC4xebfxpzu8mUSJAA4c-TuNV2H0n3ds9ZVUw5zK9IYzUKkdHV41dM5Oku_oa9VLxoC0W3w_wcB, adwords, 889604337, 44105047185, 208592463809)"""

print(data_insert) # leaving this to compare against in the Output below.
print("\n") # line break just for space while testing

# Transformation Step 1: at every ", " replace with "', '"
data_insert_p1 = data_insert.replace(", ","\', \'")
# print(data_insert_p1)

# Transformation Step 2: at every "\(" replace with "\('"
# turns out I dont need to escape this at all in Python. /shrug
data_insert_p2 = data_insert_p1.replace("(","('")
#print(data_insert_p2)

# Transformation Step 3: at every "\)" replace with "'\'),"
data_insert_p3 = data_insert_p2.replace(")","'),")
#print(data_insert_p3)

# Transformation Step 4: replace '0000-00-00' with '1901-01-01'
#  This step may not be required if Thom's format changes.
data_insert_p4 = data_insert_p3.replace("0000-00-00","1901-01-01")
#print(data_insert_p4)

# Transformation Step 5:  Trim the last character (the hanging "," at the end of the string). I could remove this step from being necessary if I make the replace() in Step 3 off of )\n? Then the last ) will need a line for itself to receive a single quote before the closing parantheses.
data_insert_p5 = data_insert_p4[:-1]
print(data_insert_p5)



"""
Here's the SQL I'm gonna need to pass the values into then run. Use sqlalchemy or something?

-- I should define a variable that is the string used after VALUES in Step 2 so I can just copy the values at the top instead of below.

/*
Inserting data with duplicate IDs is gonna be an issue. What I need to do is first get a list of all [e_id]'s, see if this list matches a temporary table of new [e_id]s, truncate the existing and then add all from DEV.
*/


/*

-- 1. TRUNCATE the DEV table
TRUNCATE TABLE [dbo].[wheretostay_conversions]

-- 2. Insert the daily data from the email into DEV
INSERT INTO wheretostay_conversions (e_id, created_date, sold_date, status, commission, gclid, custom_channel, custom_campaign, custom_adgroup, custom_ad)
 VALUES
('56851', '2017-08-05 15:44:58', '2017-08-13', 'sold', '1207.50', 'CjwKEAjw--DLBRCN_bW36taJkhwSJABSMEduMhJL-NxfBjy3DIl8Jog9rI4ObCQ-dnG4mXyFJHXpIxoCmxTw_wcB', 'adwords', '889604337', '44105051505', '208592418140'),
('56839', '2017-08-03 20:04:24', '2017-08-14', 'sold', '1190.00', 'EAIaIQobChMIsN_p16S81QIVBINpCh1PHQ8EEAAYASAAEgIpO_D_BwE', 'adwords', '901390551', '43882660934', '211750551501'),
('56927', '2017-08-14 21:09:58', '1901-01-01', 'entered', '875.00', 'CLLo0dvF19UCFcmIswodc7EKZw', 'adwords', '907860379', '48062788231', '214875939806'),
('56926', '2017-08-14 19:17:23', '1901-01-01', 'entered', '1157.14', 'Cj0KCQjwlMXMBRC1ARIsAKKGuwj7tLezQpN_8S-8cKfkwj2qO0PO918ZUHE-OV5e4EFusF-rHAofPdwaAt0qEALw_wcB', 'adwords', '885704867', '43968377506', '207755067488'),
('56907', '2017-08-12 15:09:40', '1901-01-01', 'working', '1015.00', 'Cj0KCQjwq7XMBRCDARIsAKVI5Qa9JkCO4ux2Uu9YeNJU1AKXz5wtAGGWK4F7-t_3_Y_etHiZPWfASdQaAr32EALw_wcB', 'adwords', '889604337', '44105048545', '211209447265'),
('56911', '2017-08-13 14:52:42', '1901-01-01', 'working', '3220.00', 'CjwKCAjwk4vMBRAgEiwA4ftLs4NXIgmpdekwoRHcrb2icpTfoYEN5hcg2P_rHQIce_Qv0y-H_ysgzRoCLy0QAvD_BwE', 'adwords', '893226458', '40097820850', '208900565262'),
('56834', '2017-08-03 10:09:06', '1901-01-01', 'hot', '771.43', 'EAIaIQobChMIyZyPi4W71QIV1zyBCh1pXQ2gEAAYAyAAEgJHNvD_BwE', 'adwords', '895567671', '44798392036', '209511737243'),
('56844', '2017-08-04 19:12:35', '1901-01-01', 'hot', '3571.43', 'CjwKEAjwtpDMBRC4xebfxpzu8mUSJAA4c-TuNV2H0n3ds9ZVUw5zK9IYzUKkdHV41dM5Oku_oa9VLxoC0W3w_wcB', 'adwords', '889604337', '44105047185', '208592463809')

-- 3. Show what's in the DEV table
SELECT * FROM [dbo].[wheretostay_conversions] order by [e_id]

-- 4. Find Matching [e_id]s in Dev and Prod then DELETE from PROD where match exists.

DELETE t1
FROM [dbo].[ES_W2S_Offline_Conversions] t1
INNER JOIN [dbo].[wheretostay_conversions] t2 on t1.[e_id]=t2.[e_id]
-- confirm deletion in right table
-- SELECT *   FROM [dbo].[ES_W2S_Offline_Conversions] order by [e_id]

-- 5. Insert all from DEV into PROD.

INSERT INTO [dbo].[ES_W2S_Offline_Conversions]
SELECT * FROM [dbo].[wheretostay_conversions]

-- 6. Show what's in PROD


SELECT 'DEV' as 'Dev' ,* FROM [dbo].[wheretostay_conversions] order by [e_id]
SELECT 'PROD' as 'PROD' ,*   FROM [dbo].[ES_W2S_Offline_Conversions] order by [e_id]

*/





/*

---- DEV Table ------
SELECT [e_id]
      ,[created_date]
      ,[sold_date]
      ,[status]
      ,[commission]
      ,[gclid]
      ,[custom_channel]
      ,[custom_campaign]
      ,[custom_adgroup]
      ,[custom_ad]
  FROM [dbo].[wheretostay_conversions]
    order by [e_id] desc

  ---- PROD Table ----
  SELECT [e_id]
      ,[created_date]
      ,[sold_date]
      ,[status]
      ,[commission]
      ,[gclid]
      ,[custom_channel]
      ,[custom_campaign]
      ,[custom_adgroup]
      ,[custom_ad]
  FROM [dbo].[ES_W2S_Offline_Conversions]
  order by [e_id] desc


*/
"""