'''
AnalysisPDF类
对每个PDF进行分析
'''
import os
import datetime
from django.conf import settings

from common.custom.myPDF import MyPDF
from common.custom.excel_processor import write_indicators_to_excel

class AnalysisPDF():
    '''
    描述：对每个PDF进行分析
    参数：
        filepath: string pdf文件路径
        indicators: list[dict] 指标列表
        w1: int 贡献度1
        w2: int 贡献度2
        w3: int 贡献度3
        excel_base_path: string excel文件存放路径
    '''

    def __init__(self, filepath, indicators, w1, w2, w3, excel_base_path) -> None:
        self.filepath = filepath
        self.indicators = indicators
        self.w1 = w1
        self.w2 = w2
        self.w3 = w3
        self.excel_base_path = excel_base_path
        self.date = datetime.datetime.now().strftime('%Y%m%d')

        self.pdf = MyPDF(self.filepath, media_root=settings.MEDIA_ROOT) # 提取PDF内容存储到self.pdf.documnet_info

        self.example_result = {
            "company": "龙湖",
            "company_code": "123456",
            "filepath": "path/to/file",
            "indicators": [
                {
                    "指标主题": "指标主题",
                    "需求目的": "需求目的",
                    "具体指标": [
                        {
                            "具体指标名称": "具体指标名称",
                            "三级指标": [
                                {
                                    "name": "三级指标名称",
                                    "keywords": "碳排放，中和",
                                    "文字内容": "碳排放碳排放碳排放碳排放",
                                    "图片数量": 18,
                                    "表格数量": 15
                                }
                            ]
                        },
                    ]
                },
            ],
        }

        # 初始化结果
        self.result = {}

        # 获取公司名字
        self.company_name = self.get_company_name()
        self.result["company"] = self.company_name

        # 获取公司股票代码
        self.company_code = self.get_company_code()
        self.result["company_code"] = self.company_code

        # Execl文件保存路径
        self.execl_filename = f"{self.company_code}_{self.company_name}_{self.date}.xlsx"
        self.execl_filepath = os.path.join(self.excel_base_path, self.execl_filename)

        # 每个指标进行分析, 结果保存到 self.indicators 中
        for indicator_level_1 in self.indicators:
            for indicator_level_2 in indicator_level_1["具体指标"]:
                for indicator_level_3 in indicator_level_2["三级指标"]:
                    # TODO
                    indicator_level_3["文字内容"] = ""
                    indicator_level_3["图片数量"] = 0
                    indicator_level_3["表格数量"] = 0
                    print(indicator_level_3)

        self.result["indicators"] = self.indicators
        self.result["filepath"] = self.execl_filepath
        # write_indicators_to_excel(self.execl_filepath, self.result["indicators"])

    def get_company_name(self):
        '''
        描述：获取公司名字
        返回值：
            company_name: string 公司名字
        '''
        company = os.path.basename(self.filepath)
        company = company.split('.')[0]  # "股票代码_公司名称.pdf"
        company_name = company.split('_')[1]
        return company_name

    def get_company_code(self):
        '''
        描述：获取公司股票代码
        返回值：
            company: string 公司股票代码
        '''
        company = os.path.basename(self.filepath)
        company = company.split('.')[0]  # "股票代码_公司名称.pdf"
        company_code = company.split('_')[0]
        return company_code


if __name__ == "__main__":
    # 测试
    w1, w2, w3 = 1, 1, 1
    filepath = "D:/ALL/项目/碳信息披露/测试pdf/002916_深南电路_2021.PDF"
    excel_base_path = "D:/ALL/项目/碳信息披露/CarbonInfoSystem/media/ownloads/"
    
    
    indicators = [
            {
                "指标主题": "股东和投资者",
                "需求目的": "投资与融资决策依据；企业低碳战略及管理决策依据",
                "具体指标": [
                    {
                        "具体指标名称": "碳排放风险与机遇",
                        "三级指标": [
                            {
                                "name": "碳减排过程中的风险识别与评估",
                                "keywords": "环境风险、环保风险、碳中和风险、能源风险、节能风险、风险"
                            },
                            {
                                "name": "气候变化给企业带来的财务风险",
                                "keywords": "成本节约、财务风险、成本增加、价格、浮动"
                            },
                            {
                                "name": "企业碳排放所受的政府管制风险",
                                "keywords": "政策风险、法律风险、法规风险"
                            },
                            {
                                "name": "碳减排可能给企业带来的机遇",
                                "keywords": "机遇、成本节约、减少成本、降低成本、增加收入、应对"
                            },
                            {
                                "name": "碳汇过程中的可逆性风险（如森林火灾等）",
                                "keywords": "森林火灾"
                            }
                        ]
                    }
                    ]
            }
            ]
    

    indicators = [
        {
            "指标主题": "指标主题",
            "需求目的": "需求目的",
            "具体指标": [
                {
                    "具体指标名称": "具体指标名称",
                    "三级指标": [
                        {
                            "name": "三级指标名称",
                            "keywords": "碳排放，中和",
                        }
                    ]
                },
            ]
        },
    ]
    analysis_pdf = AnalysisPDF(filepath, indicators, w1, w2, w3, excel_base_path)

