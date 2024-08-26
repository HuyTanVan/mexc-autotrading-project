from selenium.webdriver.common.by import By

"""  
    Each class contains specific elements to locate elements on mexc.com
"""
class AddsLocator:
    popovermsg = (By.XPATH, "ant-popover-message-title")

class LoginLocator:
    """
    Locators for login process.
    It includes the process of destroying pop-up adds.
    """
    adds = (By.XPATH, "//button[@class='ant-modal-close']")
    login_btn = (By.XPATH, "//a[@class='header_registerBtn__fsUiv header_authBtn__Gch60']")
    email_input_box = (By.XPATH, "//input[@id='emailInputwwwmexccom']")
    next_btn = (By.XPATH, "//div[@class='Form_buttonWrapper__o2bfF']")
    password = (By.XPATH, "//input[@id='passwordInput']")
    login = (By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-lg']")
    switch_ver_ops = (By.XPATH, "//a[@class='SignInAuthCode_securityReset__WJ1A8']")
    email_ver = (By.XPATH, "//div[@class='verification-item']")
    get_code = (By.XPATH, "//span[@class='send-verification-code_linkButton__9FR98']")

    code_boxs = (By.XPATH, "//div[@class='SignInAuthCode_codeInput__mHBbh react-code-input']")

    anti_phising_warning = (By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-lg']")
    warning_btn = (By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-lg ant-btn-block']")
    next_warning_btn = (By.XPATH, "//span[@class='NoviceGuidance_modalCancel__6hvXO']")
    right_warning = (By.XPATH, "//div[@class='GuidePopupModal_right__ZFYjo']//div[@class='GuidePopupModal_Button__0VIdm']")

class FutureLocator:
    future_btn = (By.XPATH, "//div[@class='header_leftWrapper__n8MUL']//div[3]")

    # search a contract by name
    search_contract_btn = (By.XPATH, "//div[@class='ant-dropdown-trigger contractDetail_contractNameBox__IcVlT']")
    search_contract_input = (By.XPATH, "(//input[@placeholder='Search'])[2]")
    contract_btn = (By.XPATH, "//span[@class='Pairs_row__XKonK']")

    # Levarage locators
    current_leverage =  (By.XPATH, "//div[@class='LeverageEdit_short__O_DEb LeverageEdit_leverage_simple__hVJBh']//span[@class='LeverageEdit_leverageText__jlDf0']")
    open_levarage_btn = (By.XPATH, "//div[@class='LeverageEdit_short__O_DEb LeverageEdit_leverage_simple__hVJBh']")
    levarage_slider_value = (By.XPATH, "//div[@class='LeverageEdit_short__O_DEb LeverageEdit_leverage_simple__hVJBh']")
    levarage_slider = (By.XPATH, "//div[@class='ant-slider-handle']")

    second = (By.XPATH, "//div[@class='ant-slider-handle ant-slider-handle-dragging ant-tooltip-open']")
    leverage_input = (By.XPATH, "//input[@class='LeverageProgress_leverageInput__iWDFl']")
    confirm_levarage_btn = (By.XPATH, "//button[@class='ant-btn ant-btn-primary']")
    
    # amount available locator
    available_amount = (By.XPATH, "//div[@id='mexc_contract_v_open_position']//div[@class='AssetsItem_left__cH1iU noviceGuidanceStep1']")

    # order quantity locator: USDT
    quantity_input = (By.XPATH, "//div[@id='mexc_contract_v_open_position']//input[@type='text']")

    # tp/sl checkboxes, inputs and buttons locators.
    # using same tp/sl path for both long and short.
    long_TPSL_checkbox = (By.XPATH, "(//input[contains(@type,'checkbox')])[3]")
    short_TPSL_checkbox = (By.XPATH, "(//input[contains(@type,'checkbox')])[4]")
    tp_input = (By.XPATH, "(//input[@type='text'])[4]")
    sl_input = (By.XPATH, "(//input[@type='text'])[5]")

    open_long_btn = (By.XPATH, "//button[@class='ant-btn ant-btn-default component_longBtn__BBkFR']")
    open_short_btn = (By.XPATH, "//button[@class='ant-btn ant-btn-default component_shortBtn__s8HK4']")

    # Since an order is placed, these elements are used to keep track of the order.
    # Open position: used to check if there is an order or not
    open_pos = (By.XPATH, "//div[@id='rc-tabs-0-tab-1']")
    flash_close_btn = (By.XPATH, "(//div[@class='FastClose_handleWrapper__4NFBR FastClose_short__dT1BB'])[1]")
    orders_trades_his_btn = (By.XPATH, "(//div[@class='ant-tabs-tab ant-tabs-tab-active'])[1]")
    open_pos_btn = (By.XPATH, "(//div[@class='ant-tabs-tab'])[1]")
    # current trading pair locator
    trading_pair = (By.XPATH, "//tr[@class='ant-table-row ant-table-row-level-0']//td[1]")
    # current price locator
    position = (By.XPATH, "//tr[@class='ant-table-row ant-table-row-level-0']//td[2]")
    # entry price locator
    entry_pr = (By.XPATH, "//tr[@class='ant-table-row ant-table-row-level-0']//td[3]")
    
    # Interval locators
    intervals = (By.XPATH, "//div[@class='klineInterval_klineActions__pQU2S']//div[@class='klineInterval_favInterval__5M7S6']")
    current_interval = (By.XPATH, "//div[@class='klineInterval_klineActions__pQU2S']//div[@class='klineInterval_favInterval__5M7S6 klineInterval_activeInterval__4JeuW']")

    # dummy code.
    real_time_price = (By.XPATH, "(//span[@class='market_bigPrice__yD9AA'])[1]")
    add_tp_sl_btn = (By.XPATH, "//span[@class='TpslRecordAndBtn_addBtnBox__i_fTS']")