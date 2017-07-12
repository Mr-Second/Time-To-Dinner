var React = require('react')
import EmojiShow from './emojiShow.jsx'
import LikeButton from './likeButton.jsx'
export default class UserComments extends React.Component{
  constructor(props) {
    super(props);
    this.state = {
      UserComment:[]
    }
  }
  componentDidMount() {
    // query留言api，自動生成出留言
    $.getJSON('/sloth/get/comment' + window.location.search + '&start=1', (json) => {
        this.setState({UserComment:json})
    })    
  }
  render() {
    return(
      <div>
        {
          this.state.UserComment.map((item, index) => (
            <div key={index} className="ui comments">
              <div className="comment">
                <a className="avatar">
                  <img src='/media/student.png'/>
                </a>
                <div className="content">
                  <b>匿名</b><p className="author"></p>
                  <div className="metadata">
                    <div className="date">{item['fields']['create']}</div>
                    <div className="rating">
                      <EmojiShow emoji={item['fields']['emotion']}/>
                    </div>
                  </div>
                  <div className="text">
                    <pre className='raw'>{item['fields']['raw']}</pre>
                  </div>
                  <LikeButton userId={this.props.userId} likeNum={item['fields']['like']}/>
                </div>
              </div>
            </div>
          ))
        }
      </div>
    )
  }
}