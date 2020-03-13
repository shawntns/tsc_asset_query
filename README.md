# 资产查询规则库 for tenable.sc

## Why this repository

原始诉求是解决tenable.sc查询规则庞杂，并时常作为局部或个人的knowledge，存在不易沟通、难维护等问题。

所以思路是将资产查询规则进行序列化处理（目前是yaml格式)，放到到github中以便community之间分享。

## 定义

综合使用下列4类Nessus Plugin以实现资产发现的全面性。

* 标准探测 (`*_standard`) - 基于Nessus标准资产Plugin

  * 注意：扫描方式不限于远程扫描、登录扫描或agent扫描

* 安装枚举 (`*_install`) - 基于Nessus标准安装枚举Plugin

* 进程枚举 (`*_process`) - 基于Nessus标准进程枚举Plugin

* 自定义探测 (`*_custom`) - 基于Custom Audit(aka. 自定义基线脚本)的个性化探测Plugin

### 自定义探测脚本

* 自定义探测基线脚本（Custom Audit File）[点击下载]

* Nessus Custom Audit [项目传送门]

## 规则文件

目前查询规则针对范围是综合多家国内企业安全团队所评出的 `The Most Vulnerable Assets`，以常见web中间件和服务为主。

* [tsc_asset.yml](tsc_asset.yml) -> *陆续会加入更多资产规则*

## 解析器

将以上yaml规则文件自动解析成 SC API query。

* [tsc_yaml.py](tsc_yaml.py)

## 可视化示例

![可视化示例](visual_sample.png)

## Credits

* HTSC Sec team
* 哈哈大侠
* Yoyo

[点击下载]:https://raw.githubusercontent.com/shawntns/ns_custom_audit/master/asset_discovery.audit
[项目传送门]:https://github.com/shawntns/ns_custom_audit
