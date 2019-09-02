class Catalog:
    save_button = "//button[@data-original-title='Save']"
    add_new_product = "//a[@data-original-title='Add New']"
    edit_product = "//a[@data-original-title='Edit']"
    delete_button = "//button[@data-original-title='Delete']"
    filter_button = "//button[@id='button-filter']"
    product_check_box = "//input[@name='selected[]']"
    product_name_filter = "filter_name"

    main_menu = "#menu-catalog"
    products = "Products"
    product_nav_tabs = "ul.nav.nav-tabs > li"
    # general_tab =
    product_name_field = "product_description[1][name]"
    product_description = "//div[@contenteditable='true']"
    meta_tag_title = "product_description[1][meta_title]"
    data_tab = "//a[@href='#tab-data']"
    model_field = "model"

#
# echo "Add $(pwd) to PYTHONPATH"
#
# export PYTHONPATH=$(pwd):$PYTHONPATH
#
# echo "Current PYTHONPATH: $PYTHONPATH"
