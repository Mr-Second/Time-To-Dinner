var React = require('react')
import EmojiShow from './emojiShow.jsx'

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
            <div className="ui comments" data-emotion={item['fields']['emotion']}>
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
                  {
                    item['fields']['likesfromuser'].includes(this.props.userId) 
                    ? 
                    <a className="ui red labeled icon button">
                      <i className="heart icon"></i>
                      <span className="like">{item['fields']['like']}</span>
                    </a>      
                    : 
                    <a className="ui basic red labeled icon button" data-value={'/sloth/get/like?id=' + item['pk']}>
                      <i className="heart icon"></i>
                      <span className="like">{item['fields']['like']}</span>
                    </a>
                  }
                </div>
              </div>
            </div>
          ))
        }
      </div>
    )
  }
}