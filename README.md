# CarbonInfoSystem

## How To Use
```
# 克隆gitee仓库
git clone https://gitee.com/nancyyyyy/CarbonInfoSystem.git
# 进入CarbonInfoSystem目录
cd CarbonInfoSystem
# 构建docker镜像
docker build --pull --rm -f "Dockerfile" -t carbon_info_system "." 
# 运行docker容器
docker run -dp PORT:10086 -v PATH2FILE:/code carbon_info_system
```

## TODO
- [ ] DEBUG = True; ALLOWED_HOSTS = []
- [ ] 日志记录
- [x] 异常处理
- [x] PDF分析 - [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)
- [x] [配置Tesseract OCR](https://zhuanlan.zhihu.com/p/420259031)
- [x] [自动同步Github仓库到Gitee仓库](https://gyx8899.gitbook.io/blog/share/syncgithubtogitee)