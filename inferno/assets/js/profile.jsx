var React = require('react')

export default class Profile extends React.Component{
	constructor(props) {
		super(props);
		this.state = {
			courseInfo: {},
		}
		this.renderCourseRadar = this.renderCourseRadar.bind(this)
	}

	renderCourseRadar(json) {
		let data = [
			{
					axes: [
					{axis: "自由", value: json['feedback_freedom']},
					{axis: "知識性", value: json['feedback_knowledgeable']},
					{axis: "氛圍", value: json['feedback_FU']},
					{axis: "成績", value: json['feedback_GPA']},
					{axis: "簡單", value: json['feedback_easy']}
					]
			}
		]
		$('#chart-container').empty();
		let chart = RadarChart.chart();
		chart.config({
			containerClass: 'radar-chart', // target with css, the default stylesheet targets .radar-chart
			w: 200,
			h: 200,
			factor: 0.9,
			factorLegend: 1,
			levels: 5,
			maxValue: 5,
			minValue: 0,
		});

		let svg = d3.select('#chart-container').append('svg')
			.attr('width', 200)
			.attr('height', 200); 

		// draw one
		svg = svg.append('g').classed('focus', 3).datum(data)
		svg.call(chart)
		d3.selectAll(".axis text").style("font-size","14px")
	}
	componentDidMount() {
		let id = location.search.split('id=')[1]
		$.getJSON( "/sloth/get/cvalue?id="+id, (result) => {
			this.setState({courseInfo:result})
			this.renderCourseRadar(result);
		})
	}
	render() {
		return(
			<div className="ui two column grid">
				<div className="eight wide column">
					<h3 className="ui header" id='name'>{this.state.courseInfo.name}</h3>
					<p className="cinema">
						老師：<span id='teacher'>{this.state.courseInfo.teacher}</span><br/>
						課程類型：<span id='ctype'>{this.state.courseInfo.ctype}</span><br/>
						上課教材：<span id='book'>{this.state.courseInfo.book}</span><br/>
						開課系所：<span id='dept'>{this.state.courseInfo.dept}</span><br/>
						評分方式：<span id='benchmark'>{this.state.courseInfo.benchmark}</span>
					</p>
					<p>
						<i className="ui red heart outline like icon" aria-hidden="true"></i><span id='feedback_amount'>{this.state.courseInfo.feedback_amount}</span>人參與評分
					</p>
				</div>
				<div className="eight wide column" id="chart-container"></div>
			</div>
		)
	}
}