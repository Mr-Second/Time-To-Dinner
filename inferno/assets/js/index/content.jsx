var React = require('react')
import SideBar from './sidebar.jsx'
import Pagination from './pagination.jsx'

const ContentList = (props) => {
  return(
    <div className="twelve wide mobie eight wide tablet six wide computer column" id="courseList">
      {
        props.items.map((item, idx) => (
          <div className="ui cards" key={idx}>
            <div className="card">
              <div className="content">
                <a className="avatar" href={'/infernoWeb/sloth/inside?id='+item['pk']}>
                    <img className="right floated mini ui image" src={item['fields']['avatar']}/>
                  </a>
                  <a className="avatar" href={'/infernoWeb/sloth/inside?id='+item['pk']}>
                    <div className="header shopTitle">{item['fields']['name']}</div>
                  </a>
                  <div className="meta type">
                    {item['fields']['ctype']}
                  </div>
                  <div className="description" id='School_teacher'>
                    <p className="teacher">學校：{item['fields']['school']} 老師：{item['fields']['teacher']}</p>
                  </div>
              </div>
              <div className="extra content">
                  <span className="right floated">
                    <i className="ui red heart icon"></i>
                    <span id='feedback_amount'>
                      {item['fields']['feedback_amount']+'人參與評分'}
                    </span>
                </span>
              </div>  
            </div>
          </div>
        ))
      }
    </div>
  );
}



export default class Content extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      items: [],
      pageData:{}
    }
  }
  componentDidMount() {
    $.getJSON(this.props.api, (json) => {
      const first = json.shift()
      var length = first['TotalPage']
      var school = first['school']
      var ctype = first['ctype']

      this.setState({
        items: json,
        pageData: first
      });
    })
  }
  render() {
    return (
      <div className="ui centered grid" id="InfoArea">
        <div className="row">
          <SideBar/>
          <ContentList items={this.state.items}/>              
        </div>
        <div className="row">
          <Pagination items={this.state.pageData}/>
        </div>
      </div>
    );
  }
}