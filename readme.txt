This script conver JSON-formatted windows logs from NXlog to ossec-formatted WinEvt message - after it ossec can work with this event like it is from ossec-agent

Messages from NXLog should be formatted this type:

192.168.1.12 {...}
//(ip_of_computer_with_agent) (JSON_message)

Output-type is follow:
192.168.1.12 1999-02-21 15:21:17 ...
//(ip_of_computer_with_agent) (eventttime) (ossec-formatted message)


U need make some changes in ossec decoder - replace '^WinEvt' to 'WinEvt' in windows-decoder to make it work
