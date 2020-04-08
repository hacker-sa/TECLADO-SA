#!/usr/bin/env python2
#-*- coding:utf8 -*-
import base64

sa = """IyEvdXNyL2Jpbi9lbnYgcHl0aG9uMgojLSotIGNvZGluZzp1dGY4IC0qLQppbXBvcnQgb3MKaW1w
b3J0IHN5cwppbXBvcnQgcmVhZGxpbmUKZnJvbSB0aW1lIGltcG9ydCBzbGVlcAojPT09PT09PT09
PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PQojX19f
X19fXzo6OjpfX19fOjo6Ol9fX19jb3JlcyBwcmltw6FyaWFzX19fXzo6OjpfX19fOjo6Ol9fX19f
X18KIz09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09
PT09PT09PT0KYyA9ICJcMDMzWzkwbSIKciA9ICJcMDMzWzkxbSIKZyA9ICJcMDMzWzNtXDAzM1s5
Mm0iCnkgPSAiXDAzM1s5M20iCkIgPSAiXDAzM1s5NG0iCmQgPSAiXDAzM1s5N20iCgojPT09PT09
PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PQoj
X19fOjpfX186OjpfX19fY29yZXMgc2VjdW5kw6FyaWFzIGUgdGVyw6dpw6FyaWFzX19fXzo6Ol9f
Xzo6X19fXwojPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09
PT09PT09PT09PT09PQpnbiA9ICJcMDMzWzkybSIKbSA9ICJcMDMzWzNtXDAzM1sxOzM4OzA1OzEy
OW0iCnYgPSAiXDAzM1swbVwwMzNbMTszODswNTsyMjszbSIgI3ZlcmRlIGVzY3Vybwp2YSA9ICJc
MDMzWzE7Mzg7MDU7MjNtIiAjdmVyZGUgZXNjdXJvIGNvbSBhenVsCmFjID0gIlwwMzNbM21cMDMz
WzE7Mzg7MDU7MjBtIiAjYXp1bCBjbGFybwphY24gPSAiXDAzM1swbVwwMzNbMTszODswNTsyMG0i
ICNhenVsIGNsYXJvCmFjMiA9ICJcMDMzWzE7Mzg7MDU7MjE7M20iICNhenVsY2xhcm8yCmFjMyA9
ICJcMDMzWzBtXDAzM1sxOzM4OzA1OzIxbSIgI2F6dWxjbGFybwphMiA9ICJcMDMzWzBtXDAzM1sx
OzM4OzA1OzEyOW0iCm9zLnN5c3RlbSgiY2xlYXIiKQojPT09PT09PT09PT09PT09PT09PT09PT09
PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PQojX19fX186Ojo6X19fOjo6Ol9f
X19fbW9kbyBlIHZlbG9jaWRhZGVfX19fXzo6OjpfX19fOjo6Ol9fX19fXwojPT09PT09PT09PT09
PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PQpkZWYgdGV4
dChzKToKICAgIGZvciBub29icyBpbiBzICsgIlxuIjoKICAgICAgICAgICAgc3lzLnN0ZG91dC53
cml0ZShub29icykKICAgICAgICAgICAgc3lzLnN0ZG91dC5mbHVzaCgpCiAgICAgICAgICAgIHNs
ZWVwKDUuIC8gMjEwMCkKCiM9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09
PT09PT09PT09PT09PT09PT09PT09CiNfX19fXzo6OjpfX186Ojo6X19fX2RlZmluaWNhbyBkbyBi
YW5uZXJfX19fOjo6Ol9fX186Ojo6X19fX19fCiM9PT09PT09PT09PT09PT09PT09PT09PT09PT09
PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09CmRlZiBiYW5uZXIoKToKICAgIHRleHQg
KGFjMysiIiIKCuKWrOKWrOKWrOKWrOKWrOKWrOKWrOKWrOKWrOKWrOKWrOKWrAogICAgIOKWiCAg
ICAgICDilojiloDiloDiloDiloDiloAgIOKWiOKWgOKWgOKWgOKWgOKWgOKWgOKWgCAg4paIICAg
ICAgICAg4paI4paA4paA4paA4paA4paA4paA4paA4paIICDilojiloDiloDiloDiloDiloDiloDi
loDiuJziuJwgIOKVreKWgOKWgOKWgOKWgOKWgOKWgOKVriAgICAg4paI4paA4paA4paA4paA4paA
4paAICAg4paI4paA4paA4paA4paA4paA4paA4paICiAgICAg4paIICAgICAgIOKWiCAgICAgICDi
loggICAgICAgICDiloggICAgICAgICDiloggICAgICAg4paIICDiloggICAgICAgIOKWiCAg4paI
ICAgICAg4paIICAgICDiloggICAgICAgICDiloggICAgICDilogKICAgICDiloggICAgICAg4paI
4pas4pas4pas4pas4pasICDiloggICAgICAgICDiloggICAgICAgICDilojilqzilqzilqzilqzi
lqzilqzilqziloggIOKWiCAgICAgICAg4paIICDiloggICAgICDilogg4pas4pas4pasIOKVmuKV
kOKVkOKVkOKVkOKVkOKVlyAgIOKWiOKWrOKWrOKWrOKWrOKWrOKWrOKWiAogICAgIOKWiCAgICAg
ICDiloggICAgICAg4paIICAgICAgICAg4paIICAgICAgICAg4paIICAgICAgIOKWiCAg4paIICAg
ICAgICDiloggIOKWiCAgICAgIOKWiCAgICAgICAgICAg4pWRICAg4paIICAgICAg4paICiAgICAg
4paIICAgICAgIOKWiCAgICAgICDiloggICAgICAgICDiloggICAgICAgICDiloggICAgICAg4paI
ICDiloggICAgICAgIOKWiCAg4paIICAgICAg4paIICAgICAgICAgICDiloggICDiloggICAgICDi
logKICAgICDiloggICAgICAg4paA4paA4paA4paA4paA4paAICDiloDiloDiloDiloDiloDiloDi
loDiloAgIOKWgOKWgOKWgOKWgOKWgOKWgOKWgCAgIOKWiCAgICAgICDiloggIOKWgOKWgOKWgOKW
gOKWgOKWgOKWgOKWgOK4jeK4jSAg4pWw4paA4paA4paA4paA4paA4paA4pWvICAgICDiloDiloDi
loDiloDiloDiloDiloAgICDiloggICAgICDilogKICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIiIiK2crImNyZWF0ZWQgYnkg
8J+RiSBoYWNrZXItc2EiK3ZhKyIiIgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHZlcnNpb246MS4w
CiIiIikKCgojPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09
PT09PT09PT09PT09PQojIiIiX19fX19fXzo6OjpfX186Ojo6X19fX18gbWVudSAyIF9fX19fOjo6
Ol9fX186Ojo6X19fX19fXyIiIgojPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09
PT09PT09PT09PT09PT09PT09PT09PT09PQpkZWYgbWVudTIoKToKICAgIG9zLnN5c3RlbSgnY2xl
YXInKQogICAgcHJpbnQgKGFjbisiXG5lc2NvbGhhIGEgb3DDp8OjbyDwn5GHIikKICAgIHByaW50
IChnKyIiIgoKIiIiK2EyKyJbIit5KyIxIithMisiXSIrIiIiCiAgICIiIithY24rIlxfX19fX19f
X19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX18iK2crIiIiCiIiIithY24rIiIiICAg4pWR
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICDilZEKIiIiK2FjbisiICAg4pWR
IitnKyIgIEVTQyAgIC8gICAtICAgSE9NRSAgIFVQICAgRU5EICBQR1VQICIrYWNuKyIiIuKVkQog
ICDilZEgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIOKVkQoiIiIrYWNuKyIg
ICDilZEiK2crIiBUQUIgQ1RSTCBBTFQgIExFRlQgIERPV04gIFJJR0hUIFBHRE4gIithY24rIiIi
4pWRCiAgIOKVkSIiIithY24rIl9fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19f
4pWRIithMisiIiIKCiIiIisiWyIreSsiMiIrYTIrIl0iKyIiIgogICAiIiIrYWNuKyJcX19fX19f
X19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fXyIrZysiIiIKIiIiK2FjbisiIiIgICDi
lZEgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICDilZEKIiIiK2FjbisiICAg
4pWRIitnKyIgIHsgICAgfSAgICBbICAgICBdICAgICB1cCAgICAoICAgICkgIithY24rIiIiIOKV
kQogICDilZEgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICDilZEKIiIiK2Fj
bisiICAg4pWRIitnKyIgRVNDICAgLyAgICAtICAgSE9NRSAgICArICAgIEVORCAgUEdVUCAiK2Fj
bisiIiLilZEKICAg4pWRICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg4pWR
CiIiIithY24rIiAgIOKVkSIrZysiIFRBQiBDVFJMICBBTFQgIExFRlQgIERPV04gIFJJR0hUIFBH
RE4gIithY24rIiIi4pWRCiAgIOKVkSIiIithY24rIl9fX19fX19fX19fX19fX19fX19fX19fX19f
X19fX19fX19fX19fX+KVkSIrYTIrIiIiCgoiIiIrIlsiK3krIjMiK2EyKyJdIisiIiIKICAgIiIi
K2FjbisiXF9fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fXyIrZysi
IiIKIiIiK2FjbisiIiIgICDilZEgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgIOKVkQoiIiIrYWNuKyIgICDilZEiK2crIiAgIHsgICAgfSAgICBbICAgIF0gICAgKiAg
ICAgdXAgICAoICAgICkgIithY24rIiIiIOKVkQogICDilZEgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgIOKVkQoiIiIrYWNuKyIgICDilZEiK2crIiBFU0MgICAvICAg
IC0gICA9ICAgIEhPTUUgICAgKyAgICBFTkQgIFBHVVAgIithY24rIiIi4pWRCiAgIOKVkSAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg4pWRCiIiIithY24rIiAgIOKV
kSIrZysiIFRBQiBDVFJMICBBTFQgIOKVkCAgICBMRUZUICBET1dOICBSSUdIVCBQR0ROICIrYWNu
KyIiIuKVkQogICDilZEiIiIrYWNuKyJfX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19f
X19fX19fX19fX+KVkSIrYTIrIiIiCgoiIiIrIlsiK3krIjQiK2EyKyJdIisiIiIKICAgIiIiK2Fj
bisiXF9fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX18iK2crIiIiCiIiIith
Y24rIiIiICAg4pWRICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg4pWRCiIi
IithY24rIiAgIOKVkSIrZysiICB7fSAgIFtdICAgKCkgICAgJCAgICAgVVAgICAgICMgICAgXyAi
K2FjbisiIiIg4pWRCiAgIOKVkSAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
IOKVkQoiIiIrYWNuKyIgICDilZEiK2crIiBFU0MgICAvICAgIC0gICBIT01FICAgICsgICAgRU5E
ICBQR1VQICIrYWNuKyIiIuKVkQogICDilZEgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICDilZEKIiIiK2FjbisiICAg4pWRIitnKyIgVEFCIENUUkwgIEFMVCAgTEVGVCAgRE9X
TiAgUklHSFQgUEdETiAiK2FjbisiIiLilZEKICAg4pWRIiIiK2FjbisiX19fX19fX19fX19fX19f
X19fX19fX19fX19fX19fX19fX19fX19f4pWRIithMisiIiIKCiIiIisiWyIreSsiNSIrYTIrIl0i
KyIiIgogICAiIiIrYWNuKyJcX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19f
X19fX18iK2crIiIiCiIiIithY24rIiIiICAg4pWRICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgIOKVkQoiIiIrYWNuKyIgICDilZEiK2crIiAge30gICBbXSAgICgpICAg
KiAgICAkICAgICBVUCAgICAgIyAgICBfICIrYWNuKyIiIiDilZEKICAg4pWRICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIOKVkQoiIiIrYWNuKyIgICDilZEiK2crIiBF
U0MgICAvICAgIC0gICA9ICAgSE9NRSAgICArICAgIEVORCAgUEdVUCAiK2FjbisiIiLilZEKICAg
4pWRICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIOKVkQoiIiIrYWNu
KyIgICDilZEiK2crIiBUQUIgQ1RSTCAgQUxUICDilZAgICBMRUZUICBET1dOICBSSUdIVCBQR0RO
ICIrYWNuKyIiIuKVkQogICDilZEiIiIrYWNuKyJfX19fX19fX19fX19fX19fX19fX19fX19fX19f
X19fX19fX19fX19fX19f4pWRIithMisiIiIKCiIiIisiWyIreSsiNiIrYTIrIl0iKyIiIgogICAi
IiIrYWNuKyJcX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19f
X19fX19fX19fX19fX19fX18iK2crIiIiCiIiIithY24rIiIiICAg4pWRICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIOKVkQoiIiIr
YWNuKyIgICDilZEiK2duKyIgIOKVlCAgICAgICDilZcgICAg4paAICAgIOKWiCAgICDilZEgICAg
4pWtICAgICDila4gICAgIFVQICAgICDilI8gICAgIOKUkyAgICDilLsgICIrYWNuKyIiIiDilZEK
ICAg4pWRICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgIOKVkQoiIiIrYWNuKyIgICDilZEiK2duKyIgIOKVmiAgICAgICDilZ0gICAg
4paSICAgIOKWkSAgICDilZAgICAg4pWwICAgICDila8gICAgICsgICAgICDilJcgICAgIOKUmyAg
IFBHVVAgIithY24rIiIi4pWRCiAgIOKVkSAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICDilZEKIiIiK2FjbisiICAg4pWRIitnbisi
IENUUkwgICAgIOKVoCAgICDilaMgICAg4paLICAgIOKUuyAgICDiuI0gICBMRUZUICAgRE9XTiAg
UklHSFQgICDiuJwgICBQR0ROICIrYWNuKyIiIuKVkQogICDilZEiIiIrYWNuKyJfX19fX19fX19f
X19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19f4pWR
IithMisiIiIKCiIiIisiWyIreSsiNyIrYTIrIl0iK2crIiBzb2JyZSIrIiIiCiIiIithMisiWyIr
eSsiOCIrYTIrIl0iK2crIiIiIHNhaXIiIiIpCgogICAgcHJpbnQgKGEyKQoKIz09PT09PT09PT09
PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0KIyIiIl9f
X19fXzo6Ol9fX186Ojo6X19fX18gdGVjbGFkbyAxIF9fX19fXzo6OjpfX19fOjo6X19fX18iIiIK
Iz09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09
PT09PT0KZGVmIG0xKCk6CiAgICBvcy5zeXN0ZW0oImNsZWFyIikKICAgIHByaW50KHYrIlxuYWRp
Y2lvbmFuZG8gdGVjbGFzIGVzcGVjaWFpcyBwYXJhIG8gdGVybXV4ICIpCiAgICBwcmludChhYysi
UHJvY2Vzc2FuZG8uLi4iKQogICAgcHJpbnQoeSsi4pWQIio1MikKICAgIHNsZWVwKDEpCiAgICBw
cmludChhMisiWyIreSsiISIrYTIrIl0iK3YrIiBSZWN1cGVyYW5kbyBhcnF1aXZvIHByZWRldGVy
bWluYWRvIGRvIHRlcm11eCAiK2QrIlsiK2duKyLiiJoiK2QrIl0iKyIiKQogICAgc2xlZXAoMSkK
ICAgIHRyeToKCiAgICAgb3MubWtkaXIoIi9kYXRhL2RhdGEvY29tLnRlcm11eC9maWxlcy9ob21l
Ly50ZXJtdXgiKQogICAgZXhjZXB0OgogICAgICAgIHBhc3MKCiAgICBwcmludChhMisiWyIreSsi
ISIrYTIrIl0iK2FjKyIgc3VjZXNzbyAiK2QrIlsiK2duKyLiiJoiK2QrIl0iKQogICAgc2xlZXAo
MSkKICAgIHByaW50KGEyKyJbIit5KyIhIithMisiXSIrdisiIGFkaWNpb25hbmRvIGJvdMO1ZXMg
bm8gdGVjbGFkbyBwcmVkZXRlcm1pbmFkbyAiK2QrIlsiK2duKyLiiJoiK2QrIl0iKQogICAgc2xl
ZXAoMSkKCiAgICB3aXRoICBvcGVuKCIvZGF0YS9kYXRhL2NvbS50ZXJtdXgvZmlsZXMvaG9tZS8u
dGVybXV4L3Rlcm11eC5wcm9wZXJ0aWVzIiwidyIpIGFzIHRwOgogICAgICAgdHAud3JpdGUoIiIi
ZXh0cmEta2V5cyA9IFtbIkVTQyIsIi8iLCItIiwiSE9NRSIsIlVQIiwiRU5EIiwiUEdVUCJdLFsi
VEFCIiwiQ1RSTCIsIkFMVCIsIkxFRlQiLCJET1dOIiwiUklHSFQiLCJQR0ROIl1dIiIiKQogICAg
ICAgdHAuY2xvc2UoKQoKICAgIHNsZWVwKDEpCiAgICBwcmludChhMisiWyIreSsiISIrYTIrIl0i
K2FjKyIgdGVybWluYW5kbyBwcm9jZXNzby4uIitkKyJbIitnbisi4oiaIitkKyJdIikKICAgIHNs
ZWVwKDIpCiAgICBwcmludChhMisiWyIreSsiISIrYTIrIl0iK3YrIiBTw7MgbWFpcyB1bSBzZWd1
bmRvICIrZCsiWyIrZ24rIuKImiIrZCsiXSIpCiAgICBzbGVlcCgyKQogICAgb3Muc3lzdGVtKCJ0
ZXJtdXgtcmVsb2FkLXNldHRpbmdzIikKICAgIHByaW50KGEyKyJbIit5KyIhIithMisiXSIrYWMr
IiBQcm9jZXNzbyBjb21wbGV0byIrZCsiWyIrZ24rIuKImiIrZCsiXSIpCiAgICBwcmludChhMisi
WyIreSsiISIrYTIrIl0iK0IrIiBwb3Ig8J+RiSBIQUNLRVItU0EhICIpCiAgICBwcmludCh5KyLi
lZAiKjUyKQogICAgcHJpbnQgKGcrIk9CUzogcHV4ZSBvIHRlY2xhZG8gZGEgZGlyZWl0YSBwYXJh
IGEgZXNxdWVyZGEgcGFyYSBlbnRyYXIgbmEgw6FyZWEgZGUgIHRyYWJhbGhvISEhIikKICAgIHBy
aW50ICIiCgojPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09
PT09PT09PT09PT09PQojIiIiX19fX19fOjo6X19fXzo6OjpfX19fXyB0ZWNsYWRvIDIgX19fX19f
Ojo6Ol9fX186OjpfX19fXyIiIgojPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09
PT09PT09PT09PT09PT09PT09PT09PT09PQpkZWYgbTIoKToKICAgIG9zLnN5c3RlbSgiY2xlYXIi
KQogICAgcHJpbnQodisiXG5hZGljaW9uYW5kbyB0ZWNsYXMgZXNwZWNpYWlzISIpCiAgICBwcmlu
dChhYysiUHJvY2Vzc2FuZG8uLi4iKQogICAgcHJpbnQoeSsi4pWQIio1MikKICAgIHNsZWVwKDEp
CiAgICBwcmludChhMisiWyIreSsiISIrYTIrIl0iK3YrIiBSZWN1cGVyYW5kbyBhcnF1aXZvIHBy
ZWRldGVybWluYWRvIGRvIHRlcm11eCAiK2QrIlsiK2duKyLiiJoiK2QrIl0iKQogICAgc2xlZXAo
MSkKICAgIHRyeToKICAgICBvcy5ta2RpcigiL2RhdGEvZGF0YS9jb20udGVybXV4L2ZpbGVzL2hv
bWUvLnRlcm11eCIpCiAgICBleGNlcHQ6CiAgICAgICAgcGFzcwogICAgcHJpbnQoYTIrIlsiK3kr
IiEiK2EyKyJdIithYysiIHN1Y2Vzc28gIitkKyJbIitnbisi4oiaIitkKyJdIikKICAgIHNsZWVw
KDEpCiAgICBwcmludChhMisiWyIreSsiISIrYTIrIl0iK3YrIiBhZGljaW9uYW5kbyBib3TDtWVz
IG5vIHRlY2xhZG8gcHJlZGV0ZXJtaW5hZG8gIitkKyJbIitnbisi4oiaIitkKyJdIikKICAgIHNs
ZWVwKDEpCgogICAgd2l0aCAgb3BlbigiL2RhdGEvZGF0YS9jb20udGVybXV4L2ZpbGVzL2hvbWUv
LnRlcm11eC90ZXJtdXgucHJvcGVydGllcyIsInciKSBhcyB0cDoKICAgICAgIHRwLndyaXRlKCIi
ImV4dHJhLWtleXMgPSBbWyJ7IiwifSIsIlsiLCJdIiwiVVAiLCIoIiwiKSJdLFsiRVNDIiwiLyIs
Ii0iLCJIT01FIiwiKyIsIkVORCIsIlBHVVAiXSxbIlRBQiIsIkNUUkwiLCJBTFQiLCJMRUZUIiwi
RE9XTiIsIlJJR0hUIiwiUEdETiJdXSIiIikKICAgICAgIHRwLmNsb3NlKCkKCiAgICBzbGVlcCgx
KQogICAgcHJpbnQoYTIrIlsiK3krIiEiK2EyKyJdIithYysiIHRlcm1pbmFuZG8gcHJvY2Vzc28u
LiIrZCsiWyIrZ24rIuKImiIrZCsiXSIpCiAgICBzbGVlcCgyKQogICAgcHJpbnQoYTIrIlsiK3kr
IiEiK2EyKyJdIit2KyIgU8OzIG1haXMgdW0gc2VndW5kbyAiK2QrIlsiK2duKyLiiJoiK2QrIl0i
KQogICAgc2xlZXAoMykKICAgIG9zLnN5c3RlbSgidGVybXV4LXJlbG9hZC1zZXR0aW5ncyIpCiAg
ICBwcmludChhMisiWyIreSsiISIrYTIrIl0iK2FjKyIgUHJvY2Vzc28gY29tcGxldG8gIitkKyJb
Iitnbisi4oiaIitkKyJdIikKICAgIHByaW50KGEyKyJbIit5KyIhIithMisiXSIrQisiIHBvciDw
n5GJIEhBQ0tFUi1TQSEgIikKICAgIHByaW50KHkrIuKVkCIqNTIpCiAgICBwcmludCAoZysiT0JT
OiBwdXhlIG8gdGVjbGFkbyBkYSBkaXJlaXRhIHBhcmEgYSBlc3F1ZXJkYSBwYXJhIGVudHJhciBu
YSDDoXJlYSBkZSAgdHJhYmFsaG8hISEiKQogICAgcHJpbnQgIiIKCiM9PT09PT09PT09PT09PT09
PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09CiMiIiJfX19fX186
OjpfX19fOjo6Ol9fX19fIHRlY2xhZG8gMyBfX19fX186Ojo6X19fXzo6Ol9fX19fIiIiCiM9PT09
PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09
CmRlZiBtMygpOgogICAgb3Muc3lzdGVtKCJjbGVhciIpCiAgICBwcmludCh2KyJcbmFkaWNpb25h
bmRvIHRlY2xhcyBlc3BlY2lhaXMhIikKICAgIHByaW50KGFjKyJQcm9jZXNzYW5kby4uLiIpCiAg
ICBwcmludCh5KyLilZAiKjUyKQogICAgc2xlZXAoMSkKICAgIHByaW50KGEyKyJbIit5KyIhIith
MisiXSIrdisiIFJlY3VwZXJhbmRvIGFycXVpdm8gcHJlZGV0ZXJtaW5hZG8gZG8gdGVybXV4ICIr
ZCsiWyIrZ24rIuKImiIrZCsiXSIpCiAgICBzbGVlcCgxKQogICAgdHJ5OgogICAgIG9zLm1rZGly
KCIvZGF0YS9kYXRhL2NvbS50ZXJtdXgvZmlsZXMvaG9tZS8udGVybXV4IikKICAgIGV4Y2VwdDoK
ICAgICAgICBwYXNzCiAgICBwcmludChhMisiWyIreSsiISIrYTIrIl0iK2FjKyIgc3VjZXNzbyAi
K2QrIlsiK2duKyLiiJoiK2QrIl0iKQogICAgc2xlZXAoMSkKICAgIHByaW50KGEyKyJbIit5KyIh
IithMisiXSIrdisiIGFkaWNpb25hbmRvIGJvdMO1ZXMgbm8gdGVjbGFkbyBwcmVkZXRlcm1pbmFk
byAiK2QrIlsiK2duKyLiiJoiK2QrIl0iKQogICAgc2xlZXAoMSkKCiAgICB3aXRoICBvcGVuKCIv
ZGF0YS9kYXRhL2NvbS50ZXJtdXgvZmlsZXMvaG9tZS8udGVybXV4L3Rlcm11eC5wcm9wZXJ0aWVz
IiwidyIpIGFzIHRwOgogICAgICAgdHAud3JpdGUoIiIiZXh0cmEta2V5cyA9IFtbInsiLCJ9Iiwi
WyIsIl0iLCIqIiwiVVAiLCIoIiwiKSJdLFsiRVNDIiwiLyIsIi0iLCI9IiwiSE9NRSIsIisiLCJF
TkQiLCJQR1VQIl0sWyJUQUIiLCJDVFJMIiwiQUxUIiwi4pWQIiwiTEVGVCIsIkRPV04iLCJSSUdI
VCIsIlBHRE4iXV0iIiIpCiAgICAgICB0cC5jbG9zZSgpCgogICAgc2xlZXAoMSkKICAgIHByaW50
KGEyKyJbIit5KyIhIithMisiXSIrYWMrIiB0ZXJtaW5hbmRvIHByb2Nlc3NvLi4iK2QrIlsiK2du
KyLiiJoiK2QrIl0iKQogICAgc2xlZXAoMikKICAgIHByaW50KGEyKyJbIit5KyIhIithMisiXSIr
disiIFPDsyBtYWlzIHVtIHNlZ3VuZG8gIitkKyJbIitnbisi4oiaIitkKyJdIikKICAgIHNsZWVw
KDMpCiAgICBvcy5zeXN0ZW0oInRlcm11eC1yZWxvYWQtc2V0dGluZ3MiKQogICAgcHJpbnQoYTIr
IlsiK3krIiEiK2EyKyJdIithYysiIFByb2Nlc3NvIGNvbXBsZXRvICIrZCsiWyIrZ24rIuKImiIr
ZCsiXSIpCiAgICBwcmludChhMisiWyIreSsiISIrYTIrIl0iK0IrIiBwb3Ig8J+RiSBIQUNLRVIt
U0EhICIpCiAgICBwcmludCh5KyLilZAiKjUyKQogICAgcHJpbnQgKGcrIk9CUzogcHV4ZSBvIHRl
Y2xhZG8gZGEgZGlyZWl0YSBwYXJhIGEgZXNxdWVyZGEgcGFyYSBlbnRyYXIgbmEgw6FyZWEgZGUg
IHRyYWJhbGhvISEhIikKICAgIHByaW50ICIiCgojPT09PT09PT09PT09PT09PT09PT09PT09PT09
PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PQojIiIiX19fX19fOjo6X19fXzo6Ojpf
X19fXyB0ZWNsYWRvIDQgX19fX19fOjo6Ol9fX186OjpfX19fXyIiIgojPT09PT09PT09PT09PT09
PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PQpkZWYgbTQoKToK
ICAgIG9zLnN5c3RlbSgiY2xlYXIiKQogICAgcHJpbnQodisiXG5hZGljaW9uYW5kbyB0ZWNsYXMg
ZXNwZWNpYWlzIHBhcmEgbyB0ZXJtdXggIikKICAgIHByaW50KGFjKyJwcm9jZXNzYW5kby4uLiIp
CiAgICBwcmludCh5KyLilZAiKjUyKQogICAgc2xlZXAoMSkKICAgIHByaW50KGEyKyJbIit5KyIh
IithMisiXSIrdisiIFJlY3VwZXJhbmRvIGFycXVpdm8gcHJlZGV0ZXJtaW5hZG8gZG8gdGVybXV4
ICIrZCsiWyIrZ24rIuKImiIrZCsiXSIpCiAgICBzbGVlcCgxKQogICAgdHJ5OgoKICAgICBvcy5t
a2RpcigiL2RhdGEvZGF0YS9jb20udGVybXV4L2ZpbGVzL2hvbWUvLnRlcm11eCIpCiAgICBleGNl
cHQ6CiAgICAgICAgIHBhc3MKCiAgICBwcmludChhMisiWyIreSsiISIrYTIrIl0iK2FjKyIgc3Vj
ZXNzbyAiK2QrIlsiK2duKyLiiJoiK2QrIl0iKQogICAgc2xlZXAoMSkKICAgIHByaW50KGEyKyJb
Iit5KyIhIithMisiXSIrdisiIGFkaWNpb25hbmRvIGJvdMO1ZXMgbm8gdGVjbGFkbyBwcmVkZXRl
cm1pbmFkbyAiK2QrIlsiK2duKyLiiJoiK2QrIl0iKQogICAgc2xlZXAoMSkKCiAgICB3aXRoICBv
cGVuKCIvZGF0YS9kYXRhL2NvbS50ZXJtdXgvZmlsZXMvaG9tZS8udGVybXV4L3Rlcm11eC5wcm9w
ZXJ0aWVzIiwidyIpIGFzIHRwOgogICAgICAgdHAud3JpdGUoIiIiZXh0cmEta2V5cyA9IFtbInt9
IiwiW10iLCIoKSIsIiQiLCJVUCIsIiMiLCJfIl0sWyJFU0MiLCIvIiwiLSIsIkhPTUUiLCIrIiwi
RU5EIiwiUEdVUCJdLFsiVEFCIiwiQ1RSTCIsIkFMVCIsIkxFRlQiLCJET1dOIiwiUklHSFQiLCJQ
R0ROIl1dIiIiKQogICAgICAgdHAuY2xvc2UoKQoKICAgIHNsZWVwKDEpCiAgICBwcmludChhMisi
WyIreSsiISIrYTIrIl0iK2FjKyIgdGVybWluYW5kbyBwcm9jZXNzby4uIitkKyJbIitnbisi4oia
IitkKyJdIikKICAgIHNsZWVwKDIpCiAgICBwcmludChhMisiWyIreSsiISIrYTIrIl0iK3YrIiBT
w7MgbWFpcyB1bSBzZWd1bmRvICIrZCsiWyIrZ24rIuKImiIrZCsiXSIpCiAgICBzbGVlcCgyKQog
ICAgb3Muc3lzdGVtKCJ0ZXJtdXgtcmVsb2FkLXNldHRpbmdzIikKICAgIHByaW50KGEyKyJbIit5
KyIhIithMisiXSIrYWMrIiBQcm9jZXNzbyBjb21wbGV0byAiK2QrIlsiK2duKyLiiJoiK2QrIl0i
KQogICAgcHJpbnQoYTIrIlsiK3krIiEiK2EyKyJdIitCKyIgcG9yIPCfkYkgSEFDS0VSLVNBISAi
KQogICAgcHJpbnQoeSsi4pWQIio1MikKICAgIHByaW50IChnKyJPQlM6IHB1eGUgbyB0ZWNsYWRv
IGRhIGRpcmVpdGEgcGFyYSBhIGVzcXVlcmRhIHBhcmEgZW50cmFyIG5hIMOhcmVhIGRlICB0cmFi
YWxobyEhISIpCiAgICBwcmludCAiIgoKCiM9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09
PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09CiMiIiJfX19fXzo6Ol9fXzo6OjpfX19fX19f
IHRlY2xhZG8gNSBfX19fX19fOjo6Ol9fXzo6Ol9fX19fIiIiCiM9PT09PT09PT09PT09PT09PT09
PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09CmRlZiBtNSgpOgogICAg
b3Muc3lzdGVtKCJjbGVhciIpCiAgICBwcmludCh2KyJcbmFkaWNpb25hbmRvIHRlY2xhcyBlc3Bl
Y2lhaXMgcGFyYSBvIHRlcm11eCAiKQogICAgcHJpbnQoYWMrInByb2Nlc3NhbmRvLi4uIikKICAg
IHByaW50KHkrIuKVkCIqNTIpCiAgICBzbGVlcCgxKQogICAgcHJpbnQoYTIrIlsiK3krIiEiK2Ey
KyJdIit2KyIgUmVjdXBlcmFuZG8gYXJxdWl2byBwcmVkZXRlcm1pbmFkbyBkbyB0ZXJtdXggIitk
KyJbIitnbisi4oiaIitkKyJdIikKICAgIHNsZWVwKDEpCiAgICB0cnk6CgogICAgIG9zLm1rZGly
KCIvZGF0YS9kYXRhL2NvbS50ZXJtdXgvZmlsZXMvaG9tZS8udGVybXV4IikKICAgIGV4Y2VwdDoK
ICAgICAgICAgcGFzcwoKICAgIHByaW50KGEyKyJbIit5KyIhIithMisiXSIrYWMrIiBzdWNlc3Nv
ICIrZCsiWyIrZ24rIuKImiIrZCsiXSIpCiAgICBzbGVlcCgxKQogICAgcHJpbnQoYTIrIlsiK3kr
IiEiK2EyKyJdIit2KyIgYWRpY2lvbmFuZG8gYm90w7VlcyBubyB0ZWNsYWRvIHByZWRldGVybWlu
YWRvICIrZCsiWyIrZ24rIuKImiIrZCsiXSIpCiAgICBzbGVlcCgxKQoKICAgIHdpdGggIG9wZW4o
Ii9kYXRhL2RhdGEvY29tLnRlcm11eC9maWxlcy9ob21lLy50ZXJtdXgvdGVybXV4LnByb3BlcnRp
ZXMiLCJ3IikgYXMgdHA6CiAgICAgICB0cC53cml0ZSgiIiJleHRyYS1rZXlzID0gW1sie30iLCJb
XSIsIigpIiwiKiIsIiQiLCJVUCIsIiMiLCJfIl0sWyJFU0MiLCIvIiwiLSIsIj0iLCJIT01FIiwi
KyIsIkVORCIsIlBHVVAiXSxbIlRBQiIsIkNUUkwiLCJBTFQiLCLilZAiLCJMRUZUIiwiRE9XTiIs
IlJJR0hUIiwiUEdETiJdXSIiIikKICAgICAgIHRwLmNsb3NlKCkKCiAgICBzbGVlcCgxKQogICAg
cHJpbnQoYTIrIlsiK3krIiEiK2EyKyJdIithYysiIHRlcm1pbmFuZG8gcHJvY2Vzc28uLiIrZCsi
WyIrZ24rIuKImiIrZCsiXSIpCiAgICBzbGVlcCgyKQogICAgcHJpbnQoYTIrIlsiK3krIiEiK2Ey
KyJdIit2KyIgU8OzIG1haXMgdW0gc2VndW5kbyAiK2QrIlsiK2duKyLiiJoiK2QrIl0iKQogICAg
c2xlZXAoMikKICAgIG9zLnN5c3RlbSgidGVybXV4LXJlbG9hZC1zZXR0aW5ncyIpCiAgICBwcmlu
dChhMisiWyIreSsiISIrYTIrIl0iK2FjKyIgUHJvY2Vzc28gY29tcGxldG8gIitkKyJbIitnbisi
4oiaIitkKyJdIikKICAgIHByaW50KGEyKyJbIit5KyIhIithMisiXSIrQisiIHBvciDwn5GJIEhB
Q0tFUi1TQSEgIikKICAgIHByaW50KHkrIuKVkCIqNTIpCiAgICBwcmludCAoZysiT0JTOiBwdXhl
IG8gdGVjbGFkbyBkYSBkaXJlaXRhIHBhcmEgYSBlc3F1ZXJkYSBwYXJhIGVudHJhciBuYSDDoXJl
YSBkZSAgdHJhYmFsaG8hISEiKQogICAgcHJpbnQgIiIKCgojPT09PT09PT09PT09PT09PT09PT09
PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PQojIiIiX19fXzo6OjpfX186
Ojo6X19fX19fX3RlY2xhZG8gNiBfX19fX19fOjo6Ol9fX186Ojo6X19fXyIiIgojPT09PT09PT09
PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PQpkZWYg
bTYoKToKICAgIG9zLnN5c3RlbSgiY2xlYXIiKQogICAgcHJpbnQgKHYrIlxuZXN0ZSDDqSB1bSB0
ZWNsYWRvIGVzcGVjaWFsbWVudGUgcGFyYSBkZXNlbmhvcyIpCiAgICBwcmludChhYysiUHJvY2Vz
c2FuZG8uLi4iKQogICAgcHJpbnQoeSsi4pWQIio1MikKICAgIHNsZWVwKDEpCiAgICBwcmludChh
MisiWyIreSsiISIrYTIrIl0iK3YrIiBSZWN1cGVyYW5kbyBhcnF1aXZvIHByZWRldGVybWluYWRv
IGRvIHRlcm11eCAiK2QrIlsiK2duKyLiiJoiK2QrIl0iKQogICAgc2xlZXAoMSkKICAgIHRyeToK
ICAgICBvcy5ta2RpcigiL2RhdGEvZGF0YS9jb20udGVybXV4L2ZpbGVzL2hvbWUvLnRlcm11eCIp
CiAgICBleGNlcHQ6CiAgICAgICAgcGFzcwogICAgcHJpbnQoYTIrIlsiK3krIiEiK2EyKyJdIith
YysiIHN1Y2Vzc28gIitkKyJbIitnbisi4oiaIitkKyJdIikKICAgIHNsZWVwKDEpCiAgICBwcmlu
dChhMisiWyIreSsiISIrYTIrIl0iK3YrIiBhZGljaW9uYW5kbyBib3TDtWVzIG5vIHRlY2xhZG8g
cHJlZGV0ZXJtaW5hZG8gIitkKyJbIitnbisi4oiaIitkKyJdIikKICAgIHNsZWVwKDEpCgogICAg
d2l0aCAgb3BlbigiL2RhdGEvZGF0YS9jb20udGVybXV4L2ZpbGVzL2hvbWUvLnRlcm11eC90ZXJt
dXgucHJvcGVydGllcyIsInciKSBhcyB0cDoKICAgICAgIHRwLndyaXRlKCIiImV4dHJhLWtleXMg
PSBbWyLilZQgIiwi4pWXIiwi4paAIiwi4paIIiwi4pWRIiwi4pWtIiwi4pWuIiwiVVAiLCLilI8i
LCLilJMiLCLilqwiXSxbIuKVmiAiLCLilZ0iLCLilpIiLCLilpEiLCLilZAiLCLilbAiLCLila8i
LCIrIiwi4pSXIiwi4pSbICIsIlBHVVAiXSxbIkNUUkwiLCLilaAiLCLilaMgIiwi4paLIiwi4pS7
Iiwi4riNIiwiTEVGVCIsIkRPV04iLCJSSUdIVCIsIuK4nCIsIlBHRE4iXV0iIiIpCiAgICAgICB0
cC5jbG9zZSgpCgogICAgc2xlZXAoMSkKICAgIHByaW50KGEyKyJbIit5KyIhIithMisiXSIrYWMr
IiB0ZXJtaW5hbmRvIHByb2Nlc3NvLi4iK2QrIlsiK2duKyLiiJoiK2QrIl0iKQogICAgc2xlZXAo
MikKICAgIHByaW50KGEyKyJbIit5KyIhIithMisiXSIrdisiIFPDsyBtYWlzIHVtIHNlZ3VuZG8g
IitkKyJbIitnbisi4oiaIitkKyJdIikKICAgIHNsZWVwKDMpCiAgICBvcy5zeXN0ZW0oInRlcm11
eC1yZWxvYWQtc2V0dGluZ3MiKQogICAgcHJpbnQoYTIrIlsiK3krIiEiK2EyKyJdIithYysiIFBy
b2Nlc3NvIGNvbXBsZXRvICIrZCsiWyIrZ24rIuKImiIrZCsiXSIpCiAgICBwcmludChhMisiWyIr
eSsiISIrYTIrIl0iK0IrIiBwb3Ig8J+RiSBIQUNLRVItU0EhICIpCiAgICBwcmludCh5KyLilZAi
KjUyKQogICAgcHJpbnQgKGcrIk9CUzogcHV4ZSBvIHRlY2xhZG8gZGEgZGlyZWl0YSBwYXJhIGEg
ZXNxdWVyZGEgcGFyYSBlbnRyYXIgbmEgw6FyZWEgZGUgIHRyYWJhbGhvISEhIikKICAgIHByaW50
ICIiCgoKIz09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09
PT09PT09PT09PT0KIyIiIl9fX19fX186Ojo6X19fOjo6Ol9fX19fXyBhYm91dCBfX19fX186Ojo6
X19fOjo6Ol9fX19fX18iIiIKIz09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09
PT09PT09PT09PT09PT09PT09PT09PT0KZGVmIG03KCk6CiAgICBvcy5zeXN0ZW0oImNsZWFyIikK
ICAgIHByaW50ICgiXG4iKQogICAgcHJpbnQgKHkrIioiICogNTApCiAgICBwcmludCAoZysiXG5U
RUNMQURPLVNBICIreSsiICAgICAgICAgIithYysiICAgICAgIHZlcnPDo286Iit5KyIxLjAiKQog
ICAgcHJpbnQgKGFjKyJjcmlhZG8gcG9yOiIreSsiIGhhY2tlci1zYSAgIithYysiICAgIERBVEE6
Iit5KyIwMy8wNC8yMDIwIikKICAgIHByaW50ICgiIikKICAgIHByaW50IChhYysibWV1IGdpdGh1
YiDwn5GJIit5KyIgaHR0cHM6Ly9naXRodWIuY29tL2hhY2tlci1zYSAiKQogICAgcHJpbnQgKCIi
KQogICAgcHJpbnQgKCIqIiAqIDUwKQogICAgcHJpbnQgKGEyKyJbIit5KyIxIithMisiXSIrZysi
dm9sdGFyIGFvIG1lbnUgYW50ZXJpb3IiKQogICAgcHJpbnQgKGEyKyJbIit5KyIyIithMisiXSIr
Zysic2FpciIpCiAgICBvcHQyID0gcmF3X2lucHV0KCIgbyBxdcOqIGRlc2VqYSBmYXplcj8g8J+R
iSAiKQogICAgaWYgb3B0MiBpbiBbIjEiXSBvciBvcHQyIGluIFsiMDEiXToKICAgICAgIHJlc3Rh
cnQoKQoKICAgIGVsaWYgb3B0MiBpbiBbIjIiXSBvciBvcHQyIGluIFsiMDIiXToKICAgICAgIHNh
aXIoKQoKICAgIGVsc2U6CiAgICAgICAgIG9zLnN5c3RlbSgiY2xlYXIiKQogICAgICAgICBwcmlu
dCAoZytvcHQrQisiIG7Do28gw6kgdW1hIG9ww6fDo28gZXhpc3RlbnRlIikKICAgICAgICAgcHJp
bnQgKEIrInZvbHRhbmRvIGFvIG1lbnUgcHJpbmNpcGFsLi4uIikKICAgICAgICAgc2xlZXAoMykK
ICAgICAgICAgcmVzdGFydCgpCgojPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09
PT09PT09PT09PT09PT09PT09PT09PT09PQojIiIiX19fOjo6X19fXzo6OjpfX19fIG1vZG8gZSB2
ZWxvY2lkYWRlMiBfX19fOjo6Ol9fXzo6Ol9fXyIiIgojPT09PT09PT09PT09PT09PT09PT09PT09
PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PQpkZWYgdHh0KHMpOgogICAgZm9y
IG5vb2JzIGluIHMgKyAiXG4iOgogICAgICAgICAgICBzeXMuc3Rkb3V0LndyaXRlKG5vb2JzKQog
ICAgICAgICAgICBzeXMuc3Rkb3V0LmZsdXNoKCkKICAgICAgICAgICAgc2xlZXAoMTEwLiAvIDIx
MDApCgoKIz09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09
PT09PT09PT09PT0KIyIiIl9fX19fX186OjpfX19fOjo6Ol9fXyBtZW51IGRlIHNhw61kYSBfXzo6
OjpfX19fOjo6X19fX19fIiIiCiM9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09
PT09PT09PT09PT09PT09PT09PT09PT09CmRlZiBzYWlyKCk6CiAgICBwcmludCAoZysicXVhbCBv
IHNldSBub21lPyIpCiAgICBub21lID0gcmF3X2lucHV0KCJub21lIPCfkYkgIikKICAgIG9zLnN5
c3RlbSgiY2xlYXIiKQogICAgdHh0KGcrIlxuT2zDoSAiK25vbWUrIiBtdWl0byBvYnJpZ2FkbyBw
b3IgdXNhciBlc3RhIGZlcnJhbWVudGEhISEg8J+RjyBjcmllaSBlc3RlIFxudGVjbGFkbyBwYXJh
IGZhY2lsaXRhciBhIHByb2dyYW1hw6fDo28gY29tIHJlbGHDp8OjbyAgYW8gdXNvIGRvcyBjYXLD
oWN0ZXJzXG5lIG1vdmltZW50YcOnw6NvIGRvIGN1cnNvciBuYSBob3JhIGRlIHByb2dyYW1hci4i
KQogICAgc2xlZXAoMSkKICAgIHR4dChnKyJFc3Blcm8gdMOqLWxvIGFqdWRhZG8uLi5RdWFscXVl
ciBkw7p2aWRhIGNyw610aWNhIG91IHN1amVzdMOjbyBwb3IgZmF2b3JcbmNvbnRhdGUtbWUg8J+R
iSIrYTIrIiBoYWNrZXItc2EwMkBnbWFpbC5jb20iKQogICAgdHh0KGcrIm1ldSBnaXRodWIg8J+R
iSAiK2EyKyJodHRwczovL2dpdGh1Yi5jb20vaGFja2VyLXNhIikKICAgIHN5cy5leGl0KCkKCiM9
PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09
PT09CiMiIiJfX19fX19fOjo6X19fOjo6Ol9fX2Z1bsOnw6NvIHJlc3RhcnQgX186Ojo6X19fXzo6
Ol9fX19fX18iIiIKIz09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09
PT09PT09PT09PT09PT09PT0KZGVmIHJlc3RhcnQoKToKICAgIHIgPSBzeXMuZXhlY3V0YWJsZQog
ICAgb3MuZXhlY2wociwgciwgKiBzeXMuYXJndikKCmRlZiBmbigpOgogICAgcHJpbnQgKHkrImRl
c2VqYSB0ZXN0YXIgbWFpcyBhbGd1bSB0ZWNsYWRvPyIpCiAgICBwcmludCAoYTIrIlsiK3krIjEi
K2EyKyJdIithY24rIiB0ZXN0YXIiKQogICAgcHJpbnQgKGEyKyJbIit5KyIyIithMisiXSIrYWNu
KyIgc2FpciIpCiAgICBvcHQgPSByYXdfaW5wdXQoeSsib3DDp8OjbyDwn5GJICIpCiAgICBpZiBv
cHQgaW4gWyIxIl0gb3Igb3B0IGluIFsiMDEiXToKICAgICAgIG1lbnUyKCkKCiAgICBlbGlmIG9w
dCBpbiBbIjIiXSBvciBvcHQgaW4gWyIwMiJdOgogICAgICAgc2FpcigpCgogICAgZWxzZToKICAg
ICAgICBvcy5zeXN0ZW0oImNsZWFyIikKICAgICAgICBwcmludCAoZytvcHQrQisiIG7Do28gw6kg
dW1hIG9ww6fDo28gZXhpc3RlbnRlIikKICAgICAgICBwcmludCAoQisidm9sdGFuZG8gYW8gbWVu
dSBwcmluY2lwYWwuLi4iKQogICAgICAgIHNsZWVwKDMpCiAgICAgICAgcmVzdGFydCgpCg=="""

eval(compile(base64.b64decode(sa),'','exec'))
