var React = require('react')
import UserComments from './userComments.jsx'

const Reply = (props) => {
	const handleSubmit = () => {
		if(props.userId==undefined){
			toastr.error('請登入後再留言')
			return
		}
		let emotion = $('#emotionDropdown').dropdown('get value')
		let comments = $('textarea').val()
		if (emotion==''){
			toastr.error('請選擇情緒')
			return
		}
		else if(comments.length<10){
			toastr.error('留言需要至少10個字')
			return
		}
		$.post(location.href, {'csrfmiddlewaretoken':getCookie('csrftoken'),'comments':comments, 'emotion':emotion, 'id':props.userId})
		.done((res)=> {
			if(res=='SORRY 目前只開放留言一次喔~~ 未來會再依照情況調整'){
				toastr.warning(res);                    
			}
			else{
				toastr.success('留言成功')
				setTimeout("location.reload();", 700)
			}
		})
		.fail(function() {
			toastr.error('請檢查是否登入或是重新整理頁面')
		})
		.always(function() {
			console.log( "reply finished" );
		});                
	}
	return(
		<div className="ten wide column">
			<h2>評論</h2>
			<UserComments userId={props.userId}/>
			<div className="ui reply form">
				<div className="field">
					<textarea placeholder="新增公開留言" name="comments"></textarea>
					<button className="ui primary button" onClick={handleSubmit}>送出</button> 
					<div className="ui floating dropdown button" id='emotionDropdown'>
						<div className="text"><i className="heart icon"></i>選擇情緒</div>
						<i className="dropdown icon"></i>
						<div className="menu">
							<a className="item" data-value='neutral'><i className="meh icon"></i>中立</a>
							<a className="item" data-value='neg'><i className="frown icon"></i>反面評論</a>
							<a className="item" data-value='pos'><i className="smile icon"></i>正面評論</a>
						</div>
					</div>
				</div>
			</div>
		</div>
	)   
}
export default  Reply