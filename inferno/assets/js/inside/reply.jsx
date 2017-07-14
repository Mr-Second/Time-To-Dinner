var React = require('react')
import UserComments from './userComments.jsx'
import { Dropdown, Button } from 'semantic-ui-react'
const emotionOptions = [
  {
    text: '中立',
    value: 'neutral',
    image: { avatar: true, src: '/assets/images/avatar/small/jenny.jpg' },
  },
  {
    text: '反面評論',
    value: 'neg',
    image: { avatar: true, src: '/assets/images/avatar/small/jenny.jpg' },
  },
  {
    text: '正面評論',
    value: 'pos',
    image: { avatar: true, src: '/assets/images/avatar/small/jenny.jpg' },
  }
]

const Reply = (props) => {
	const getCookie = (name) => {
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
					<Button>
						選擇情緒
				    <Dropdown inline options={emotionOptions} defaultValue='選擇情緒' />
				  </Button>
				</div>
			</div>
		</div>
	)   
}
export default  Reply