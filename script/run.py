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
