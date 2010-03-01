jQuery(function($) {
    // Why only store the checkbox selector below and not the result? Because
    // if another piece of JavaScript fiddles with rows on the page
    // (think AJAX delete), modifying the stored checkboxes later may fail.
    var actionForm = $('#batch-action-form');
    var checkboxSelector = 'tr input.batch-select';
    var selectButtons = actionForm.find('button[name=select_all]');
    var deselectButtons = actionForm.find('button[name=deselect_all]');
    var changer_box = actionForm.find('input#batchadmin_invert_checkbox');
    
    var checker = function(checked) {
        return function(e) {
            if (checked) {
                selectButtons.hide();
                deselectButtons.show();
            }
            else {
                deselectButtons.hide();
                selectButtons.show();
            }
            actionForm.find(checkboxSelector).each(function() {
                this.checked = checked;
                $(this).change();
            });
        }
    }

    var checker2 = function() {
        return function (e) {
            checked = this.checked;
            actionForm.find(checkboxSelector).each(function() {
                this.checked = checked;
                $(this).change();
            });
        }
    }
    selectButtons.show().click(checker(true));
    deselectButtons.click(checker(false));
    changer_box.click(checker2(changer_box.checked))
    
    // Highlight selected rows on change, and trigger the change event in
    // case any are selected by default.
    /*
    actionForm.find(checkboxSelector).change(function(e) {
        var row = $(this).parents('tr');
        if (this.checked) { row.addClass('selected'); }
        else { row.removeClass('selected'); }
    }).change();*/
});
