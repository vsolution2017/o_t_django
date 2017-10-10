function load_Mantenimiento(cbo){
    $.ajax({
        url:'/panel/mantenimiento/load/',
        type:'GET',
        async:false,
        success: function(response){
            result = '';
            $(cbo).html(result);
            $(response).each(function(i,val){
                result+= '<option value="'+ val.id +'">'+ val.descripcion +'</option>';
            });
            $(cbo).html(result);
            $(cbo).selectpicker('refresh');
        }
    });
}
function load_Parroquia(cbo){
    $.ajax({
        url:'/panel/parroquia/load/',
        type:'GET',
        async:false,
        success: function(response){
            result = '';
            $(cbo).html(result);
            $(response).each(function(i,val){
                result+= '<option value="'+ val.id +'">'+ val.descripcion +'</option>';
            });
            $(cbo).html(result);
            $(cbo).selectpicker('refresh');
        }
    });
}
function load_TipoActividad(cbo){
    $.ajax({
        url:'/panel/actividad/load/',
        type:'GET',
        async:false,
        success: function(response){
            result = '';
            $(cbo).html(result);
            $(response).each(function(i,val){
                result+= '<option value="'+ val.id +'">'+ val.descripcion +'</option>';
            });
            $(cbo).html(result);
            $(cbo).selectpicker('refresh');
        }
    });
}
function load_contratista(){
    $.ajax({
        url: '/panel/contratistas/load/',
        type: 'GET',
        async:false,
        success: function(result){
            console.log(result);
            append = "";
            $(result).each(function(i,val){
                append += '<option value="'+ val.id +'">'+ val.nombres +'</option>';
            });
            $("#cboContratista").html(append);
            $("#cboContratista").selectpicker("refresh");
        }
    });
}
