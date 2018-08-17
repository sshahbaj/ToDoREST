function eventHandlers()
{
    $("#add_item_form").submit
    (
        function(event)
        {
            event.preventDefault();
            var item_text = $("#add_item_textbox").val();
            $.ajax
            ({
                url: '',
                method: 'POST',
                data: {
                    'item_text': item_text,
                    'csrfmiddlewaretoken': '{{ csrf_token }}',
                },
                dataType: 'json',
                success: function(data)
                {
                    $('<tr>',{
                        'html': '<td>'+data.added_item_text+'</td><td><button>Delete</button></td><td><button>Update</button></td>'
                    }
                    ).appendTo('#item_table');
                    $("#add_item_textbox").val('');
                }

            });
        }
    );
    $("button.delete").click
    (
        function(event)
        {
            event.preventDefault();
            var delete_button_id = this.id;
            $.ajax
            ({
                url: '',
                method: 'POST',
                data:{
                    'delete_button_id': delete_button_id,
                    'csrfmiddlewaretoken': '{{ csrf_token }}',
                },
                dataType: 'json',
                success: function(data)
                {
                    $('#'+data.row_to_delete).remove();
                }
            });
        }
    );
}

$(document).ready(eventHandlers);