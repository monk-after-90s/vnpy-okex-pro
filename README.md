# 检查下载历史K线是否包含了当前的未完成K线


# vnpy-okex-pro

继承自[KandyYe的vnpy_okex](https://github.com/KandyYe/vnpy_okex)

获取交易产品历史K线数据改为使用OKX接口
```html
GET /api/v5/market/history-candles
```

## 安装

安装需要基于2.2.0版本以上的[VN Studio](https://www.vnpy.com)。

直接使用pip命令：

```
pip install vnpy_okex_pro
```

下载解压后在cmd中运行

```
python setup.py install
```

## 使用

以脚本方式启动（script/run.py）：

```python
import vnpy_crypto

vnpy_crypto.init()
from vnpy.event import EventEngine
from vnpy.trader.engine import MainEngine
from vnpy.trader.ui import MainWindow, create_qapp

# 上面固定不动
# ——————————————————————————————————————————————————
# Gateway
from vnpy_okex_pro import OkexGateway
# App
from vnpy_datamanager import DataManagerApp


def main():
    """主入口函数"""
    qapp = create_qapp()
    event_engine = EventEngine()
    main_engine = MainEngine(event_engine)
    # ——————————————————————————————————————————————————
    # Gateway
    main_engine.add_gateway(OkexGateway)
    # App
    main_engine.add_app(DataManagerApp)
    # ——————————————————————————————————————————————————
    main_window = MainWindow(main_engine, event_engine)
    main_window.showMaximized()

    qapp.exec()


if __name__ == "__main__":
    main()
```
