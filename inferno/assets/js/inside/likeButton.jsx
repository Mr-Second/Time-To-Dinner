var React = require('react')

export default class LikeButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      likeNum: props.likeNum,
      likesfromuser: props.likesfromuser
    }
  	this.handleLike = this.handleLike.bind(this)
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
  handleLike() {
    if(this.props.userId==null){
      toastr.error('請登入後再按讚');
      return;
    }
  	$.post('/sloth/get/like?id=' + this.props.pk, {'id':this.props.userId, 'csrfmiddlewaretoken':this.getCookie('csrftoken'),'like':(this.state.likesfromuser.includes(this.props.userId) ? -1 : 1)})
  	.done(() => {
  		this.setState({
        likeNum:this.state.likeNum + (this.state.likesfromuser.includes(this.props.userId) ? -1 : 1),
        likesfromuser: this.state.likesfromuser.includes(this.props.userId) ? this.state.likesfromuser=this.state.likesfromuser.filter(x => x!=this.props.userId) : this.state.likesfromuser=this.state.likesfromuser.concat(this.props.userId)
      })
  	})
  	.fail(function() {
  		toastr.error('請檢查是否登入，或是重新整理頁面')
  	})
  }
  
  render() {
  	return (
  		<a className={"ui red labeled icon button " + (this.state.likesfromuser.includes(this.props.userId) ? '' : 'basic') } onClick={this.handleLike}>
  		  <i className="heart icon"></i>
  		  <span className="like">{this.state.likeNum}</span>
  		</a>  
  	)
  }
}