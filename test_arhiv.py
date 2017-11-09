# encoding=utf-8

import re
import datetime
from datetime import timedelta, datetime

filedata = r'{"begin":"2017-07-18T12:09:42+03:00","end":"2017-07-18T12:09:44+03:00","state":"is_on","reports":{"packet_count":[{"ipv4":19,"ipv6":0,"name":"in"},{"ipv4":10,"ipv6":0,"name":"out"}],"processes":[{"cpu":0.0,"memory":385024,"path":"C:\\Windows\\System32\\smss.exe","pid":268},{"cpu":0.0,"memory":1966079,"path":"C:\\Windows\\System32\\csrss.exe","pid":340},{"cpu":0.0,"memory":1368064,"path":"C:\\Windows\\System32\\wininit.exe","pid":376},{"cpu":0.016206398887862454,"memory":9252864,"path":"C:\\ANM.agent\\anm-agent.exe","pid":384},{"cpu":0.0,"memory":1548288,"path":"C:\\Windows\\System32\\csrss.exe","pid":388},{"cpu":0.0,"memory":2506752,"path":"C:\\Windows\\System32\\winlogon.exe","pid":416},{"cpu":0.0,"memory":5152768,"path":"C:\\Windows\\System32\\services.exe","pid":472},{"cpu":0.0,"memory":4931584,"path":"C:\\Windows\\System32\\lsass.exe","pid":488},{"cpu":0.0,"memory":3096576,"path":"C:\\Windows\\System32\\lsm.exe","pid":496},{"cpu":0.0,"memory":3706880,"path":"C:\\Windows\\System32\\svchost.exe","pid":608},{"cpu":0.0,"memory":2969600,"path":"C:\\Windows\\System32\\VBoxService.exe","pid":664},{"cpu":0.0,"memory":3813376,"path":"C:\\Windows\\System32\\svchost.exe","pid":716},{"cpu":0.0,"memory":2420736,"path":"C:\\Windows\\System32\\winlogon.exe","pid":736},{"cpu":0.0,"memory":17182720,"path":"C:\\Windows\\System32\\svchost.exe","pid":772},{"cpu":0.0,"memory":16453632,"path":"C:\\Windows\\System32\\LogonUI.exe","pid":840},{"cpu":0.0,"memory":89423872,"path":"C:\\Windows\\System32\\svchost.exe","pid":860},{"cpu":0.0,"memory":7954432,"path":"C:\\Windows\\System32\\svchost.exe","pid":900},{"cpu":0.0,"memory":48291839,"path":"C:\\Windows\\explorer.exe","pid":916},{"cpu":0.016206398887862454,"memory":37724160,"path":"C:\\Windows\\System32\\svchost.exe","pid":936},{"cpu":0.0,"memory":30994432,"path":"C:\\Windows\\System32\\svchost.exe","pid":1072},{"cpu":0.0,"memory":7708672,"path":"C:\\Windows\\System32\\spoolsv.exe","pid":1224},{"cpu":0.0,"memory":7700480,"path":"C:\\Windows\\System32\\svchost.exe","pid":1252},{"cpu":0.0,"memory":6197248,"path":"C:\\Windows\\System32\\svchost.exe","pid":1348},{"cpu":0.0,"memory":4661248,"path":"C:\\Windows\\System32\\svchost.exe","pid":1388},{"cpu":0.0,"memory":2392064,"path":"C:\\Windows\\System32\\rdpclip.exe","pid":1436},{"cpu":0.008103199443931227,"memory":3457024,"path":"C:\\Windows\\System32\\wbem\\WmiPrvSE.exe","pid":1712},{"cpu":0.0,"memory":12611583,"path":"C:\\Windows\\System32\\taskhost.exe","pid":1804},{"cpu":0.0,"memory":1703936,"path":"C:\\Windows\\System32\\svchost.exe","pid":1920},{"cpu":0.0,"memory":6832127,"path":"C:\\Program Files\\Windows Media Player\\wmpnetwk.exe","pid":1952},{"cpu":0.0,"memory":8355840,"path":"C:\\Windows\\System32\\sppsvc.exe","pid":1976},{"cpu":0.0,"memory":4042752,"path":"C:\\Windows\\System32\\taskhost.exe","pid":2024},{"cpu":0.032412797775724908,"memory":30445568,"path":"C:\\totalcmd\\TOTALCMD64.EXE","pid":2092},{"cpu":0.0,"memory":26464256,"path":"C:\\Windows\\System32\\mmc.exe","pid":2124},{"cpu":0.0,"memory":1445888,"path":"C:\\Windows\\System32\\conhost.exe","pid":2252},{"cpu":0.0,"memory":78639104,"path":"C:\\Windows\\System32\\svchost.exe","pid":2344},{"cpu":0.0,"memory":20381696,"path":"C:\\Windows\\System32\\SearchIndexer.exe","pid":2392},{"cpu":0.0,"memory":1011712,"path":"C:\\totalcmd\\TCMADM64.EXE","pid":2536},{"cpu":0.0,"memory":1855488,"path":"C:\\Windows\\System32\\csrss.exe","pid":2544},{"cpu":0.0,"memory":1638400,"path":"C:\\Windows\\System32\\dwm.exe","pid":2660},{"cpu":0.0,"memory":1875968,"path":"C:\\Windows\\System32\\VBoxTray.exe","pid":2700},{"cpu":0.0,"memory":19832831,"path":"C:\\Program Files\\Far Manager\\Far.exe","pid":2800},{"cpu":0.0,"memory":2158592,"path":"C:\\Windows\\System32\\svchost.exe","pid":2808}],"volume_nic":[{"hw_addr":"08:00:27:48:D5:64","in":1896,"name":"Адаптер рабочего стола Intel(R) PRO/1000 MT","out":23063}]}}'

s = '2017-10-16T05:00:00+03:00' #start time
fmt = "%Y-%m-%dT%H:%M:%S+03:00" #time formatter
mytime = datetime.strptime(s, fmt)
d = timedelta(seconds=5)

inside_time_begin = mytime.strftime(fmt)
mytime = mytime + d
inside_time_end = mytime.strftime(fmt)

print(filedata)

begin = re.search(r'begin...(.*)...end', filedata).group(1)
end = re.search(r'end...(.*)...state', filedata).group(1)
new_data = filedata.replace(begin , inside_time_begin)
new_data = new_data.replace(end , inside_time_end)

print(new_data)