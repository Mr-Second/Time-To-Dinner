var React = require('react')
import Information from './information.jsx'
import Questionnaire from './questionnaire.jsx'
import ModalPage from './modalpage.jsx'
import Reply from './reply.jsx'

export default class InsidePage extends React.Component{
  constructor(props) {
    super(props);
    this.state = {
      userId: null,
    }
    this.activeMenu = this.activeMenu.bind(this)
    this.getCookie = this.getCookie.bind(this)
  }
  getCookie(name) {
      //name should be 'csrftoken', as an argument to be sent into getCookie()
     let cookieValue = null;
     if (document.cookie && document.cookie != '') {
         let cookies = document.cookie.split(';');
         for (let i = 0; i < cookies.length; i++) {
             let cookie = jQuery.trim(cookies[i]);
             // Does this cookie string begin with the name we want?
             if (cookie.substring(0, name.length + 1) == (name + '=')) {
                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                 break;
             }
         }
     }
     return cookieValue;
  }
  componentDidMount() {
    let loginUrl = "http://login.campass.com.tw"
    $.ajax({
      url: loginUrl + '/fb/user',
      dataType: 'json',
      xhrFields: {
        withCredentials: true
      },
      success: (res) => {
        $('#fb-login-btn').html('<i className="fa fa-facebook-square" aria-hidden="true"></i>登出').attr('href', loginUrl + '/fb/logout?redirect_service=www');

        // if didn't have cookie, create user first and then assign cookie
        // else, only update cookie without post to createUser. Preventing our server overload.
        if(this.getCookie('id')!=res['id']){
          $.post('/infernoWeb/createUser', Object.assign(res, {'csrfmiddlewaretoken':this.getCookie('csrftoken')}))
          .done(function(response) {
            document.cookie = `id=${res['id']}`;
          })
          .fail(function(response) {
            console.log(response)
          })
        }

        this.setState({userId:res['id']});
        $.post(location.href, Object.assign(res, {'csrfmiddlewaretoken':this.getCookie('csrftoken')}))
        .done(function(response){
          console.log('success')
        })
        .fail(function(response){
          console.log('fail')
          console.log(response)
        });
      },
      error: (res) => {
        // User is not logged in
        console.log('not login')
      }
    }); 
  };
  activeMenu(e) {
    let $target = $(e.currentTarget)
    console.log($target)
    $target
    .addClass('active')
    .closest('.ui.menu')
    .find('.item')
    .not($target)
    .removeClass('active');
    for(let i of $('div.comments')){
      console.log($(i).attr('data-emotion'))

      if ($target.attr('data-emotion')=='all'){
        $(i).css('display', '')
      }
      else if ($(i).attr('data-emotion')==$target.attr('data-emotion')){
        $(i).css('display', '')
      }
      else{
        $(i).css('display', 'none')
      }
    }
  }
  render() {
    return(
      <div className="ui centered grid">
        <Information/>
        <div className="eight wide column">
          <ModalPage/>
          <Questionnaire userId={this.state.userId}/>
          <div className="ui four item inverted menu">
            <a className="active blue item" data-emotion='all' onClick={this.activeMenu}>所有留言</a>
            <a className="blue item" data-emotion='neutral' onClick={this.activeMenu}>中立評論</a>
            <a className="blue item" data-emotion='pos' onClick={this.activeMenu}>正面評論</a>
            <a className="blue item" data-emotion='neg' onClick={this.activeMenu}>反面評論</a>
          </div>
        </div>
        <Reply userId={this.state.userId}/>
      </div>
    )   
  }
}