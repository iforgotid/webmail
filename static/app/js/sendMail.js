var currentType;
function init() {
  $('#textarea').wysihtml5();
  $('#sendType input[type=radio]').on('click',function(){
    var type = $('#sendType').find('input:checked').val();
    currentType = type;
    if(type == 'immediately') {
      $('#intervalContainer').hide();
      $('#timeContainer').hide();
    } else if(type == 'byInterval') {
      $('#intervalContainer').show();
      $('#timeContainer').hide();
    } else if(type == 'byTime') {
      $('#intervalContainer').hide();
      $('#timeContainer').show();
    }
  });
  $('#sendMail').click(function(){
    if(currentType == 'immediately') {
      sendMailImmediately();
    } else if(currentType == 'byInterval' || currentType == 'byTime') {
      createTimerForMail(currentType);
    }
  });

}
function sendMailImmediately() {
  var mailto = $('#mailto').val();
  var subject = $('#subject').val();
  var content = $('#textarea').val();
  var postData = {
    to: [
      { 'email': mailto,
        'name': 'Xue Jiaqi',
        'type': 'to'
      }
    ],
    subject: subject,
    html: content
  };
  $.ajax({
    type: "POST",
    url: '/api/sendMail',
    dataType: 'json',
    data: JSON.stringify(postData),
    success: function (data) {
      console.log(data);
    }
  })
}
function createTimerForMail(type) {
  var mailto = $('#mailto').val();
  var subject = $('#subject').val();
  var content = $('#textarea').val();
  var postData = {
    to: [
      { 'email': mailto,
        'name': 'Xue Jiaqi',
        'type': 'to'
      }
    ],
    subject: subject,
    html: content,
    type:type
  };
  if(type == 'byInterval') {
    var timeUnit = $( "#timeUnit option:selected" ).val();
    var intervalCount = Number($('#intervalCount').val());
    postData.intervalCount = intervalCount;
    postData.timeUnit = timeUnit;
  } else if(type == 'byTime') {
    var timeStr = $('#timeStr').val();
    postData.timeStr = timeStr;
  }
  $.ajax({
    type: "POST",
    url: '/api/createTimerForMail',
    dataType: 'json',
    data: JSON.stringify(postData),
    success: function (data) {
      console.log(data);
    }
  });
}

function sendMailByTime() {

}

init();