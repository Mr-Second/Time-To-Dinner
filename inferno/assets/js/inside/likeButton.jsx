var React = require('react')

export default class LikeButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { alreadyLiked: 'basic', likeNum: props.likeNum}
  	this.handleLike = this.handleLike.bind(this)
  }
  
  handleLike() {
  	const table = {
  		'basic':['', -1],
  		'':['basic', 1]
  	}
    if(this.props.userId==null){
        toastr.error('請登入後再按讚');
        return;
    }
	$.post('/sloth/get/like?id=' + item['pk'], {'id':this.props.userId, 'csrfmiddlewaretoken':getCookie('csrftoken'),'like':next})
	.done(function() {
		this.setState({alreadyLiked: table[this.state.alreadyLiked][0], likeNum:this.state.likeNum + table[this.state.alreadyLiked][1]})
	})
	.fail(function() {
		toastr.error('請檢查是否登入，或是重新整理頁面')
	})
  }
  
  render() {
  	return (
  		<a className={"ui red labeled icon button " + this.state.alreadyLiked} onClick={this.handleLike}>
  		  <i className="heart icon"></i>
  		  <span className="like">{this.props.likeNum}</span>
  		</a>  
  	)
  }
}