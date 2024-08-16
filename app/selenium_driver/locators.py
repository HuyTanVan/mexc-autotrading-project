from selenium.webdriver.common.by import By

class AddsLocator:
    popovermsg = (By.XPATH, "ant-popover-message-title")
class LoginLocator:
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
# class EmailBrowserLocator:
#     input_email_and_pass = (By.XPATH, "//input[@class='whsOnd zHQkBf']")
#     # next_btn = (By.XPATH, "//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b']")
#     next_btn = (By.XPATH,
#                  "//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 BqKGqe Jskylb TrZEUc lw1w4b']//span[@class='VfPpkd-vQzf8d']")

#     login_method = (By.XPATH, "(//div[contains(@role,'link')])[3]")
#     phone_input = (By.XPATH, "//input[@class='VfPpkd-fmcmS-wGMbrd ']")
class FutureLocator:
    future_btn = (By.XPATH, "//div[@class='header_leftWrapper__n8MUL']//div[3]")
    # search the coin by name
    search_contract_btn = (By.XPATH, "//div[@class='ant-dropdown-trigger contractDetail_contractNameBox__IcVlT']")
    search_contract_box = (By.XPATH, "//input[@placeholder='Search']")
    contract_btn = (By.XPATH, "//span[@class='Pairs_row__XKonK']")
    # levarage
    current_leverage =  (By.XPATH, "//div[@class='LeverageEdit_short__O_DEb LeverageEdit_leverage_simple__hVJBh']//span[@class='LeverageEdit_leverageText__jlDf0']")
    open_levarage_btn = (By.XPATH, "//div[@class='LeverageEdit_short__O_DEb LeverageEdit_leverage_simple__hVJBh']")
    levarage_slider_value = (By.XPATH, "//div[@class='ant-slider SliderPro_sliderPro__Dlb65 ant-slider-horizontal ant-slider-with-marks']//div[@role='slider']")
    levarage_slider = (By.XPATH, "//div[@class='ant-slider-handle']")

    second = (By.XPATH, "//div[@class='ant-slider-handle ant-slider-handle-dragging ant-tooltip-open']")
    leverage_input = (By.XPATH, "//input[@class='LeverageProgress_leverageInput__iWDFl']")
    confirm_levarage_btn = (By.XPATH, "//button[@class='ant-btn ant-btn-primary']")
    long_TPSL_btn = (By.XPATH, "(//input[contains(@type,'checkbox')])[3]")
    tp_long_box = (By.XPATH, "(//input[contains(@type,'text')])[1]")
    sl_long_box = (By.XPATH, "(//input[contains(@type,'text')])[2]")

    open_long_btn = (By.XPATH, "//button[@class='ant-btn ant-btn-default component_longBtn__BBkFR']")
    short_TPSL_btn = (By.XPATH, "(//input[contains(@type,'checkbox')])[4]")
    tp_short_box = (By.XPATH, "(//input[contains(@type,'text')])[3]")
    sl_short_box = (By.XPATH, "(//input[contains(@type,'text')])[4]")
    open_short_btn = (By.XPATH, "//button[@class='ant-btn ant-btn-default component_shortBtn__s8HK4']")

    quantity_input_box = (By.XPATH, "//div[@class='InputNumberExtend_wrapper__qxkpD extend-wrapper']//input[@class='ant-input']")

    available_amount = (By.XPATH, "//div[@id='mexc_contract_v_open_position']//div[@class='AssetsItem_left__cH1iU noviceGuidanceStep1']")

    real_time_price = (By.XPATH, "//tr[@class='ant-table-row ant-table-row-level-0']//td[3]")
    add_tp_sl_btn = (By.XPATH, "//span[@class='TpslRecordAndBtn_addBtnBox__i_fTS']")

    # Since an order is placed, these elements are used to keep track of the order.
    flash_close_btn = (By.XPATH, "(//div[@class='FastClose_handleWrapper__4NFBR FastClose_short__dT1BB'])[1]")
