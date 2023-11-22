"""web server can be configured to save log
files in different formats. One widely used format is the Common
Log Format (CLF). Format: <IP Address> <Client Id> <User Id> <Time> <Request>
<Status> <Size>
Using python regex, this code will be used to pull information from a log in the common
log format"""
import re

check = '127.0.0.1 - rj [13/Nov/2019:14:43:30] "GET HTTP/1.0" 200 2326'

"""to name group and search the IP address group in the CLF sample"""
ro_IP = re.compile(r'(?P<IP>\d+\.\d+\.\d+\.\d+)')
m_IP = ro_IP.search(check)

"""to name group and search the Time in CLF sample"""
ro_Time = re.compile(r'\[(?P<Time>\d\d/\w{3}/\d{4}:\d{2}:\d{2}:\d{2})\]')
m_Time = ro_Time.search(check)

"""to name group and search the UserID in CLF sample"""
ro_User = re.compile(r' - (?P<User>\w+)')
m_User = ro_User.search(check)

"""to name group and search the REQUEST in CLF sample"""
ro_REQUEST = re.compile(r'(?P<REQUEST>".+")')
m_REQUEST = ro_REQUEST.search(check)

"""to name group and search the STATUS CODE in CLF sample"""
ro_StatusCode = re.compile(r'(?P<STATUS_CODE>\s\d{3})')
m_StatusCode = ro_StatusCode.search(check)

"""to name group and search the SIZE in CLF sample"""
ro_SIZE = re.compile(r'(?P<SIZE>\s\d{4})')
m_SIZE = ro_SIZE.search(check)

"""print the information to the screen"""
print(f'IP ADDRESS: {m_IP.group("IP")}')
print(f'TIME: {m_Time.group("Time")}')
print(f'USERID: {m_User.group("User")}')
print(f'REQUEST: {m_REQUEST.group("REQUEST")}')
print(f'STATUS_CODE: {m_StatusCode.group("STATUS_CODE")}')
print(f'SIZE: {m_SIZE.group("SIZE")}')

