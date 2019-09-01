class Catalog:
    save_button = "//button[@data-original-title='Save']"
    add_new_product = "//a[@data-original-title='Add New']"
    edit_product = "//a[@data-original-title='Edit']"
    delete_button = "//a[data-original-title='Delete']"
    # product_check_box =

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
