var currentType = 'immediately';
function init() {
    $('#textarea').wysihtml5();
    $('#sendType input[type=radio]').on('click', function () {
        var type = $('#sendType').find('input:checked').val();
        currentType = type;
        if (type == 'immediately') {
            $('#intervalContainer').hide();
            $('#timeContainer').hide();
        } else if (type == 'byInterval') {
            $('#intervalContainer').show();
            $('#timeContainer').hide();
        } else if (type == 'byTime') {
            $('#intervalContainer').hide();
            $('#timeContainer').show();
        }
    });
    $('#sendMail').click(function () {
        if (currentType == 'immediately') {
            sendMailImmediately();
        } else if (currentType == 'byInterval' || currentType == 'byTime') {
            createTimerForMail(currentType);
        }
    });
    $("#mailto").blur(function () {
        addMailTo();
    });
    $('#mailto').keyup(function (event) {
        if (event.keyCode == 13) {
            addMailTo();
        }
    });

    $('#toMailList').on('click','.remove-mailto',function () {
        $(this).parent().remove();
        var len = $('#toMailList button').length;
        if(len == 0) {
            $('#mailListContainer').hide();
        }
    });
}
function sendMailImmediately() {
    var postData = getMailObj();
    if(!postData) {
        return;
    }
    $.ajax({
        type: "POST",
        timeout: 10 * 1000,
        url: '/api/sendMail',
        dataType: 'json',
        data: JSON.stringify(postData),
        success: function (data) {
            if(data.code == 0) {
                showMessage('success', '立即发送成功');
            } else {
                showMessage('error', '发送失败，请稍后再试');
            }
        },
        error: function(jqXHR, textStatus, errorThrown) {
            console.log(textStatus, errorThrown);
            showMessage('error', '网络繁忙，请稍后再试');
        }
    })
}
function createTimerForMail(type) {
    var postData = getMailObj();
    if(!postData) {
        return;
    }
    postData.type = type;
    if (type == 'byInterval') {
        var timeUnit = $("#timeUnit option:selected").val();
        var intervalCount = Number($('#intervalCount').val());
        postData.intervalCount = intervalCount;
        postData.timeUnit = timeUnit;
    } else if (type == 'byTime') {
        var timeStr = $('#timeStr').val();
        postData.timeStr = timeStr;
    }
    $.ajax({
        type: "POST",
        timeout: 10 * 1000,
        url: '/api/createTimerForMail',
        dataType: 'json',
        data: JSON.stringify(postData),
        success: function (data) {
            if(data.code == 0) {
                showMessage('success', '创建延时发送成功');
            } else {
                showMessage('error', '发送失败，请稍后再试');
            }
        },
        error: function(){
            showMessage('error', '网络繁忙，请稍后再试');
        }
    });
}

function getMailObj() {
    var postData = {
        to : []
        /*
        to: [
            {
                'email': mailto,
                'name': 'Xue Jiaqi',
                'type': 'to'
            }
        ],
        subject: subject,
        html: content,
        type: type
        */
    };
    var mailToLen = $('.email-text').length;
    if(mailToLen == 0) {
        showMessage('error', '请至少填写一位收件人。');
        return null;
    }
    $('.email-text').each(function(){
        var email = $(this).html();
        var obj = {
            email: email,
            type: 'to'
        }
        postData.to.push(obj);
    });
    var subject = $('#subject').val();
    if(!subject) {
        showMessage('error', '请填写邮件主题。');
        return null;
    }
    postData.subject = subject;
    var content = $('#textarea').val();
    if(!content) {
        showMessage('error', '请填写邮件正文。');
        return null;
    }
    postData.html = content;
    return postData;
}

function addMailTo() {
    var emailAddress = $('#mailto').val();
    if (emailAddress == '') {
        var len = $('#toMailList button').length;
        if(len == 0) {
            showMessage('error', '添加的收件人EMAIL不能为空');
        }
        return;
    }
    if (/^(\w)+(\.\w+)*@(\w)+((\.\w+)+)$/.test(emailAddress) === false) {
        showMessage('error', '输入的EMAIL格式不合法，请重新输入');
        return;
    }
    var html = '<button type="button" class="btn btn-info button-email"><span class="email-text">' + emailAddress + '</span>&nbsp<i class="glyphicon glyphicon-remove remove-mailto"></i></button>';
    $('#toMailList').append(html);
    $('#mailto').val('');
    $('#mailListContainer').show();
}

function showMessage(status, message) {
    var title = '信息提示';
    if (status == 'success') {
        title = '操作成功';
        $('#infoMessage').removeClass('modal-error-message').addClass('modal-info-message')
    } else if (status == 'error') {
        title = '发生错误';
        $('#infoMessage').removeClass('modal-info-message').addClass('modal-error-message')
    }
    $('#modalLabel').html(title);
    $('#infoMessage').html(message);
    $('#infoModal').modal();
}
init();