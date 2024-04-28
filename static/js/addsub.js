
$(document).on('click','#btn-add', ()=>{

    let number = $('#wrapper').children().length + 1;

    let formAdd = `
        <div class="form-row">
            <div class="form-group col-md-4">
                <label for="sub">Subscription ${number}</label>
                <select name="sub" class="form-control" id="customer">
                    <option> Choose the invoice type ... </option>
                    <option value="S">STANDARD</option>
                    <option value="P">PREMIUM</option>
                </select>
            </div>
            <div class="form-group col-md-2">
                <label for="quantity-${number}"> Quantity </label>
                <input min="1" step="1" type="number" name="quantity" id="quantity-${number}" class="form-control" required>
            </div>
            <div class="form-group col-md-3">
                <label for="unit-${number}"> Unit Price </label>
                <input min="1" step="0.01" type="number" name="unit" onchange="handleChangeSingleSub(this.id)" id="unit-${number}" class="form-control" required>
            </div>
            <div class="form-group col-md-3">
                <label for="total-sub-${number}"> Total </label>
                <input min="1" step="0.1" readonly type="number" name="total-sub" id="total-sub-${number}" class="form-control" required>
            </div>
        </div>
    `;

    $('#wrapper:last').append(formAdd);    
})

$(document).on('click','#btn-remove', ()=>{

    $("#wrapper").children().last().remove();
})


function handleChangeSingleSub(id){

    let newId = id + '';

    let listString = newId.split('-')

    let subId = listString[1];
    
    let qtyId = `#quantity-${subId}`;

    let unitId = `#unit-${subId}`;

    let totalId = `#total-sub-${subId}`;

    let totalLine = parseFloat($(qtyId).val()) * parseFloat($(unitId).val());

    $(totalId).val(totalLine);

    $("#total").val(parseFloat($('#total').val()) + totalLine)


}



