**设计思想**

- 通过requests, BeautifulSoup实现API自动化，保证后端API主要功能及业务流程

- 通过selenium实现web UI自动化，appium+stf实现android UI自动化，保证前端页面操作功能及业务流程

- 通过pytest对测试脚本进行管理，allure report 实现报告输出

- 通过jenkins实现脚本CI，tomcat实现测试报告线上化

- 使用python作为脚本语言

**设计框架(autotestFrame.png)**

![](https://github.com/jinwu18/web-app-h5-api-pyTestAutomation/blob/master/autotestFrame.png)

**说明** 

- pytest：测试用例管理

- allure：测试报告

**代码结构** 

├─framework 测试框架

│  ├─base - 自动化测试基础类

│  ├─web - web端driver管理基础类

│  ├─driver - web脚本执行基础类

│  ├─app - app脚本执行基础类

├─utils 测试工具类（文件处理等）

├─page 测试页面对象类

├─script 业务、功能脚本


**脚本执行后，通过allure生成测试报告(allure_report.png)**

![](https://github.com/jinwu18/web-app-h5-api-pyTestAutomation/blob/master/allure_report.png)

