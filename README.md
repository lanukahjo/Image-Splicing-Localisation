# Image Splicing Detection and Localization using Digital Forensics

**This project is no longer maintained.**

[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)
[![Diksha](https://img.shields.io/github/followers/diksham1?color=brightgreen&label=diksham1&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI0MCIgaGVpZ2h0PSI0MCIgdmlld0JveD0iMTIgMTIgNDAgNDAiPjxwYXRoIGZpbGw9IiNGRkZGRkYiIGQ9Ik0zMiwxMy40Yy0xMC41LDAtMTksOC41LTE5LDE5YzAsOC40LDUuNSwxNS41LDEzLDE4YzEsMC4yLDEuMy0wLjQsMS4zLTAuOWMwLTAuNSwwLTEuNywwLTMuMiBjLTUuMywxLjEtNi40LTIuNi02LjQtMi42QzIwLDQxLjYsMTguOCw0MSwxOC44LDQxYy0xLjctMS4yLDAuMS0xLjEsMC4xLTEuMWMxLjksMC4xLDIuOSwyLDIuOSwyYzEuNywyLjksNC41LDIuMSw1LjUsMS42IGMwLjItMS4yLDAuNy0yLjEsMS4yLTIuNmMtNC4yLTAuNS04LjctMi4xLTguNy05LjRjMC0yLjEsMC43LTMuNywyLTUuMWMtMC4yLTAuNS0wLjgtMi40LDAuMi01YzAsMCwxLjYtMC41LDUuMiwyIGMxLjUtMC40LDMuMS0wLjcsNC44LTAuN2MxLjYsMCwzLjMsMC4yLDQuNywwLjdjMy42LTIuNCw1LjItMiw1LjItMmMxLDIuNiwwLjQsNC42LDAuMiw1YzEuMiwxLjMsMiwzLDIsNS4xYzAsNy4zLTQuNSw4LjktOC43LDkuNCBjMC43LDAuNiwxLjMsMS43LDEuMywzLjVjMCwyLjYsMCw0LjYsMCw1LjJjMCwwLjUsMC40LDEuMSwxLjMsMC45YzcuNS0yLjYsMTMtOS43LDEzLTE4LjFDNTEsMjEuOSw0Mi41LDEzLjQsMzIsMTMuNHoiLz48L3N2Zz4%3D)](https://github.com/diksham1)
[![Kunal Ojha](https://img.shields.io/github/followers/lanukahjo?color=brightgreen&label=lanukahjo&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI0MCIgaGVpZ2h0PSI0MCIgdmlld0JveD0iMTIgMTIgNDAgNDAiPjxwYXRoIGZpbGw9IiNGRkZGRkYiIGQ9Ik0zMiwxMy40Yy0xMC41LDAtMTksOC41LTE5LDE5YzAsOC40LDUuNSwxNS41LDEzLDE4YzEsMC4yLDEuMy0wLjQsMS4zLTAuOWMwLTAuNSwwLTEuNywwLTMuMiBjLTUuMywxLjEtNi40LTIuNi02LjQtMi42QzIwLDQxLjYsMTguOCw0MSwxOC44LDQxYy0xLjctMS4yLDAuMS0xLjEsMC4xLTEuMWMxLjksMC4xLDIuOSwyLDIuOSwyYzEuNywyLjksNC41LDIuMSw1LjUsMS42IGMwLjItMS4yLDAuNy0yLjEsMS4yLTIuNmMtNC4yLTAuNS04LjctMi4xLTguNy05LjRjMC0yLjEsMC43LTMuNywyLTUuMWMtMC4yLTAuNS0wLjgtMi40LDAuMi01YzAsMCwxLjYtMC41LDUuMiwyIGMxLjUtMC40LDMuMS0wLjcsNC44LTAuN2MxLjYsMCwzLjMsMC4yLDQuNywwLjdjMy42LTIuNCw1LjItMiw1LjItMmMxLDIuNiwwLjQsNC42LDAuMiw1YzEuMiwxLjMsMiwzLDIsNS4xYzAsNy4zLTQuNSw4LjktOC43LDkuNCBjMC43LDAuNiwxLjMsMS43LDEuMywzLjVjMCwyLjYsMCw0LjYsMCw1LjJjMCwwLjUsMC40LDEuMSwxLjMsMC45YzcuNS0yLjYsMTMtOS43LDEzLTE4LjFDNTEsMjEuOSw0Mi41LDEzLjQsMzIsMTMuNHoiLz48L3N2Zz4%3D)](https://github.com/lanukahjo)
[![Anindya Kundu](https://img.shields.io/github/followers/meganindya?color=brightgreen&label=meganindya&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI0MCIgaGVpZ2h0PSI0MCIgdmlld0JveD0iMTIgMTIgNDAgNDAiPjxwYXRoIGZpbGw9IiNGRkZGRkYiIGQ9Ik0zMiwxMy40Yy0xMC41LDAtMTksOC41LTE5LDE5YzAsOC40LDUuNSwxNS41LDEzLDE4YzEsMC4yLDEuMy0wLjQsMS4zLTAuOWMwLTAuNSwwLTEuNywwLTMuMiBjLTUuMywxLjEtNi40LTIuNi02LjQtMi42QzIwLDQxLjYsMTguOCw0MSwxOC44LDQxYy0xLjctMS4yLDAuMS0xLjEsMC4xLTEuMWMxLjksMC4xLDIuOSwyLDIuOSwyYzEuNywyLjksNC41LDIuMSw1LjUsMS42IGMwLjItMS4yLDAuNy0yLjEsMS4yLTIuNmMtNC4yLTAuNS04LjctMi4xLTguNy05LjRjMC0yLjEsMC43LTMuNywyLTUuMWMtMC4yLTAuNS0wLjgtMi40LDAuMi01YzAsMCwxLjYtMC41LDUuMiwyIGMxLjUtMC40LDMuMS0wLjcsNC44LTAuN2MxLjYsMCwzLjMsMC4yLDQuNywwLjdjMy42LTIuNCw1LjItMiw1LjItMmMxLDIuNiwwLjQsNC42LDAuMiw1YzEuMiwxLjMsMiwzLDIsNS4xYzAsNy4zLTQuNSw4LjktOC43LDkuNCBjMC43LDAuNiwxLjMsMS43LDEuMywzLjVjMCwyLjYsMCw0LjYsMCw1LjJjMCwwLjUsMC40LDEuMSwxLjMsMC45YzcuNS0yLjYsMTMtOS43LDEzLTE4LjFDNTEsMjEuOSw0Mi41LDEzLjQsMzIsMTMuNHoiLz48L3N2Zz4%3D)](https://github.com/meganindya)

BTech 8th Semester Project (IT871)

## Description

![02](./reports/images/Image%20Splicing%20Localisation%20-%20Presentation-02.png)
![03](./reports/images/Image%20Splicing%20Localisation%20-%20Presentation-03.png)
![04](./reports/images/Image%20Splicing%20Localisation%20-%20Presentation-04.png)
![05](./reports/images/Image%20Splicing%20Localisation%20-%20Presentation-05.png)
![06](./reports/images/Image%20Splicing%20Localisation%20-%20Presentation-06.png)
![07](./reports/images/Image%20Splicing%20Localisation%20-%20Presentation-07.png)
![08](./reports/images/Image%20Splicing%20Localisation%20-%20Presentation-08.png)
![09](./reports/images/Image%20Splicing%20Localisation%20-%20Presentation-09.png)
![10](./reports/images/Image%20Splicing%20Localisation%20-%20Presentation-10.png)
![11](./reports/images/Image%20Splicing%20Localisation%20-%20Presentation-11.png)
![13](./reports/images/Image%20Splicing%20Localisation%20-%20Presentation-13.png)
![14](./reports/images/Image%20Splicing%20Localisation%20-%20Presentation-14.png)
![15](./reports/images/Image%20Splicing%20Localisation%20-%20Presentation-15.png)
![16](./reports/images/Image%20Splicing%20Localisation%20-%20Presentation-16.png)
![17](./reports/images/Image%20Splicing%20Localisation%20-%20Presentation-17.png)
![18](./reports/images/Image%20Splicing%20Localisation%20-%20Presentation-18.png)
![19](./reports/images/Image%20Splicing%20Localisation%20-%20Presentation-19.png)
![20](./reports/images/Image%20Splicing%20Localisation%20-%20Presentation-20.png)
![21](./reports/images/Image%20Splicing%20Localisation%20-%20Presentation-21.png)
![22](./reports/images/Image%20Splicing%20Localisation%20-%20Presentation-22.png)
![23](./reports/images/Image%20Splicing%20Localisation%20-%20Presentation-23.png)
![24](./reports/images/Image%20Splicing%20Localisation%20-%20Presentation-24.png)
![25](./reports/images/Image%20Splicing%20Localisation%20-%20Presentation-25.png)
![26](./reports/images/Image%20Splicing%20Localisation%20-%20Presentation-26.png)
![27](./reports/images/Image%20Splicing%20Localisation%20-%20Presentation-27.png)
![28](./reports/images/Image%20Splicing%20Localisation%20-%20Presentation-28.png)
![29](./reports/images/Image%20Splicing%20Localisation%20-%20Presentation-29.png)
![30](./reports/images/Image%20Splicing%20Localisation%20-%20Presentation-30.png)
![31](./reports/images/Image%20Splicing%20Localisation%20-%20Presentation-31.png)
![32](./reports/images/Image%20Splicing%20Localisation%20-%20Presentation-32.png)
