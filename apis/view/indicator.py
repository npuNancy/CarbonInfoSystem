
from common.base.base_respons import retJson


def add_indicators(request):
    '''
    描述：添加三级指标
    方法：POST
    参数：
        name: 三级指标名称 
        type: 关键词上传类型 'file' | 'keywords'
        keywords: 关键词
        file: 关键词文件 (.txt文件 一行一个关键词)
    返回值:
        name: 三级指标名称
        keywords: 关键词
    '''
    if request.method == 'GET':
        return retJson(code=0, msg="GET请求")
    elif request.method == 'POST':
        name = request.POST.get('name')
        type = request.POST.get('type')

        if type == 'file':
            file = request.FILES.get('file')
            if not file:
                return retJson(code=0, msg="请上传关键词文件")
            keywords = file.read().decode('utf-8')

        elif type == 'keywords':
            keywords = request.POST.get('keywords')
            if not keywords:
                return retJson(code=0, msg="请填写关键词")

        # 处理keywords
        keywords = keywords.replace(' ', ',')
        keywords = keywords.replace('，', ',')
        keywords = keywords.replace('、', ',')
        keywords = keywords.replace('\n', ',')
        keywords = keywords.replace('\r', ',')
        keywords = keywords.replace('\t', ',')
        keywords = keywords.replace(',,', ',')

        return retJson(code=1, msg="success", data={"name": name, "keywords": keywords})


def indicators(request):
    '''
    描述：获取指标列表
    方法：GET
    参数：
        system 
            说明: 
            system=1碳信息披露质量分析系统
            system=2企业碳中和发展分析系统
    返回值:
        指标列表
    '''
    返回值示例 = [
        {
            "指标主题": "股东和投资者",
            "需求目的": "投资与融资决策依据；企业低碳战略及管理决策依据",
            "具体指标": [
                {
                    "具体指标名称": "碳排放风险与机遇",
                    "三级指标": [
                        {
                            "name": "碳减排过程中的风险识别与评估",
                            "key_words": "碳, xxx"
                        },
                        {
                            "name": "气候变化给企业带来的财务风险",
                            "key_words": "财务, xxx"
                        },
                    ]
                },
            ]
        },
    ]

    if request.method == 'GET':
        system = int(request.GET.get('system'))
        res = {}
        if system == 1:

            return retJson(code=1, msg="success", data={"indicators": res})
        elif system == 2:

            return retJson(code=1, msg="success", data={"indicators": res})
    elif request.method == 'POST':
        return retJson(code=0, msg="POST请求")
