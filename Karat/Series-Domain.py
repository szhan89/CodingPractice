from collections import defaultdict
import numpy
#####test case
pairs = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
user1 = ["3234.html", "xys.html", "7hsaa.html"]
user2 = ["3234.html", "sdhsfjdsh.html", "xys.html", "7hsaa.html"]
completed_purchase_user_ids = ["3123122444","234111110", "8321125440", "99911063"]
ad_clicks = [
 #"IP_Address,Time,Ad_Text",
"122.121.0.1,2016-11-03 11:41:19,Buy wool coats for your pets",
"96.3.199.11,2016-10-15 20:18:31,2017 Pet Mittens",
"122.121.0.250,2016-11-01 06:13:13,The Best Hollywood Coats",
"82.1.106.8,2016-11-12 23:05:14,Buy wool coats for your pets",
"92.130.6.144,2017-01-01 03:18:55,Buy wool coats for your pets",
"92.130.6.145,2017-01-01 03:18:55,2017 Pet Mittens"]
all_user_ips = [
  #"User_ID,IP_Address",
   "2339985511,122.121.0.155",
  "234111110,122.121.0.1",
  "3123122444,92.130.6.145",
  "39471289472,2001:0db8:ac10:fe01:0000:0000:0000:0000",
  "8321125440,82.1.106.8",
  "99911063,92.130.6.144"]
#####
'''Question 1
We are given a list cpdomains of count-paired domains. 
We would like a list of count-paired domains, (in the same format as the input, and in any order), that explicitly counts the number of visits to each subdomain.
'''
def domainCounts(pairs):
    maps = defaultdict(int)
    for record in pairs:
        [count, domain] = record.split()
        domainBuild=domain.split(".") #[google, mail, com]
        for i in range(0, len(domainBuild)):
            maps[".".join(domainBuild[i:])]+=int(count)
    return dict(maps)
#print(domainCounts(pairs))
        
'''Question 2
Longest common continous subarray
    _, 3234, xyxs, 7hsaa
_.  0 , 0,     0,   0,
3234 0  1,     0,   0,
sdhsdf 0  0,    0,  0,
xys  0  0,      1,  0,
7hsaa 0 0,      0,  2

'''
def commonContinuousDomain(user1, user2):
    m = len(user1)+1
    n = len(user2)+1
    dp = numpy.zeros((m,n))
    for i in range(1, m):
        for j in range(1,n):
            if(user2[j-1]==user1[i-1]):
                dp[i][j]=dp[i-1][j-1]+1
    
    return dp[m-1][n-1]
print(commonContinuousDomain(user1, user2))

'''Question 3
// The people who buy ads on our network don't have enough data about how ads are working for
//their business. They've asked us to find out which ads produce the most purchases on their website.

// Our client provided us with a list of user IDs of customers who bought something on a landing page
//after clicking one of their ads:

// # Each user completed 1 purchase.
// completed_purchase_user_ids = [
//   "3123122444","234111110", "8321125440", "99911063"]

// And our ops team provided us with some raw log data from our ad server showing every time a
//user clicked on one of our ads:
// ad_clicks = [
//  #"IP_Address,Time,Ad_Text",
//  "122.121.0.1,2016-11-03 11:41:19,Buy wool coats for your pets",
//  "96.3.199.11,2016-10-15 20:18:31,2017 Pet Mittens",
//  "122.121.0.250,2016-11-01 06:13:13,The Best Hollywood Coats",
//  "82.1.106.8,2016-11-12 23:05:14,Buy wool coats for your pets",
//  "92.130.6.144,2017-01-01 03:18:55,Buy wool coats for your pets",
//  "92.130.6.145,2017-01-01 03:18:55,2017 Pet Mittens",
//]
       
//The client also sent over the IP addresses of all their users.
       
//all_user_ips = [
//  #"User_ID,IP_Address",
//   "2339985511,122.121.0.155",
//  "234111110,122.121.0.1",
//  "3123122444,92.130.6.145",
//  "39471289472,2001:0db8:ac10:fe01:0000:0000:0000:0000",
//  "8321125440,82.1.106.8",
//  "99911063,92.130.6.144"
//]
       
// Write a function to parse this data, determine how many times each ad was clicked,
//then return the ad text, that ad's number of clicks, and how many of those ad clicks
//were from users who made a purchase.


// Expected output:
// Bought Clicked Ad Text
// 1 of 2  2017 Pet Mittens
// 0 of 1  The Best Hollywood Coats
// 3 of 3  Buy wool coats for your pets\
    
# map - K: ads V:user-clicked
# map - K: ip V:userID
# Clicked = len(v)
# Bought len(b in v)
    
'''
def covertionRate(all_user_ips, ad_clicks, completed_purchase_user_ids):
    userIP = defaultdict(str)
    for record in all_user_ips:
        [id, ip] = record.split(",")
        userIP[id]=ip
    
    userVisit = defaultdict(list)
    for visit in ad_clicks:
        [ip_, _, ads] = visit.split(",")
        userVisit[ads].append(ip_)
    
    result = []    
    for key in userVisit:
        temp = userVisit[key]
        clicked_cts = len(temp)
        bought_cts = 0
        for bought in completed_purchase_user_ids:
            if (userIP[bought] in temp):
                bought_cts+=1
        result.append([bought_cts,clicked_cts,key])
    return result
print(covertionRate(all_user_ips, ad_clicks, completed_purchase_user_ids))