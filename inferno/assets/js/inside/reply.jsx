var React = require('react')
import UserComments from './userComments.jsx'

const Reply = (props) => {
  return(
    <div className="ten wide column">
      <h2>評論</h2>
      <UserComments userId={props.userId}/>
      <div className="ui reply form">
        <div className="field">
          <textarea placeholder="新增公開留言" name="comments"></textarea>
          <button className="ui primary button" id="reply222">送出</button> 
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