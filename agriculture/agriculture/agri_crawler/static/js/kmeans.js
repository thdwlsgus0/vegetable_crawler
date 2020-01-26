function isNumberKey(evt) {
    var charCode = (evt.which) ? evt.which : evt.keyCode;
    if (charCode != 46 && charCode > 31 &&
        (charCode < 48 || charCode > 57))
        return false;
    return true;
}
function FileUpload(){
 if(!$("#fileupload").val()){
  alert('select');
  $("#fileupload").focus();
  return;
 }
 var frm;
 frm =$("#js-upload-form");
 frm.attr("action", "/post");
 frm.submit(); 
}
function FileupladCallback(data, state){
 if(data=="error")
 {
  alert("error");
  return false;
 }
 alert("success");
}
$(function(){
 var frm=$('#js-upload-form');
 frm.ajaxFrom(FileuploadCallback);
 frm.submit(function(){return false;});
}
$(document).ready(function() {
    var chosenAttr = [];
    var uploadedfileName = "";
    var clickCounter = 0;
    var classAttr = '';
    var newItem = {};

    function cross(a, b) {
        var c = [],
            n = a.length,
            m = b.length,
            i, j;
        for (i = -1; ++i < n;)
            for (j = -1; ++j < m;) c.push({
                x: a[i],
                i: i,
                y: b[j],
                j: j
            });
        return c;
    }

    function colores_google(n) {
        var colores_g = ["#dbdbdb", "#f40909"];
        return colores_g[n % colores_g.length];
    }

    $('.tcard').click(function() {
        $('#tasks').hide(500);
        $('#algorithms').removeAttr("hidden");
    });

    $('body').bootstrapMaterialDesign();

    $('#knn').click(function() {

        var numberClust = $('#nclust').val();


        $.post("./kmapply", {
            filename: uploadedfileName,
            attributes: JSON.stringify(chosenAttr),
            ncluster: numberClust,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        }, function(data, status) {

            var result_table_data = '';
            var header = 1;

            $.each(data, function(key, value) {
                if (key >= data.length - numberClust) {

                    if (header == 1) {
                        result_table_data += '<thead><tr>'
                        $.each(data[key], function(objkey, objvalue) {
                            if (objkey != "class" && objkey != "centroid") {
                                result_table_data += '<th scope="col">' + objkey + '</th>'
                            } else if (objkey == "class" && objkey != "centroid") {
                                result_table_data += '<th scope="col">Color</th>'
                            }
                        });
                        header = 0;
                    }
                    result_table_data += '</tr></thead><tbody>'
                    $.each(data[key], function(objkey, objvalue) {
                        if (objkey != "class" && objkey != "centroid") {
                            result_table_data += '<td>' + objvalue + '</td>'
                        } else if (objkey == "class" && objkey != "centroid") {
                            result_table_data += '<td style="background-color:'+d3.schemeCategory10[objvalue]+'"></td>'
                        }
                    });
                }
            });

            result_table_data += '</tbody>';

            $('#sky-table').append(result_table_data);


            var width = 960,
                size = 200,
                padding = 40;

            var x = d3.scaleLinear()
                .range([padding / 2, size - padding / 2]);

            var y = d3.scaleLinear()
                .range([size - padding / 2, padding / 2]);

            var xAxis = d3.axisBottom()
                .scale(x)
                .ticks(6);

            var yAxis = d3.axisLeft()
                .scale(y)
                .ticks(6);

            var opacityCircles = 0.85;

            var color = d3.scaleOrdinal(d3.schemeCategory10);


            var domainByTrait = {},
                traits = d3.keys(data[0]).filter(function(d) {
                    return d !== "class" && d !== "centroid";
                }),
                n = traits.length;

            traits.forEach(function(trait) {
                domainByTrait[trait] = d3.extent(data, function(d) {
                    return d[trait];
                });
            });

            xAxis.tickSize(size * n);
            yAxis.tickSize(-size * n);

            var brush = d3.brush()
                .on("start", brushstart)
                .on("brush", brushmove)
                .on("end", brushend)
                .extent([
                    [0, 0],
                    [size, size]
                ]);

            var svg = d3.select("#graph").append("svg")
                .attr("width", size * n + padding)
                .attr("height", size * n + padding)
                .append("g")
                .attr("transform", "translate(" + padding + "," + padding / 2 + ")");

            svg.selectAll(".x.axis")
                .data(traits)
                .enter().append("g")
                .attr("class", "x axis")
                .attr("transform", function(d, i) {
                    return "translate(" + (n - i - 1) * size + ",0)";
                })
                .each(function(d) {
                    x.domain(domainByTrait[d]);
                    d3.select(this).call(xAxis);
                });

            svg.selectAll(".y.axis")
                .data(traits)
                .enter().append("g")
                .attr("class", "y axis")
                .attr("transform", function(d, i) {
                    return "translate(0," + i * size + ")";
                })
                .each(function(d) {
                    y.domain(domainByTrait[d]);
                    d3.select(this).call(yAxis);
                });

            var cell = svg.selectAll(".cell")
                .data(cross(traits, traits))
                .enter().append("g")
                .attr("class", "cell")
                .attr("transform", function(d) {
                    return "translate(" + (n - d.i - 1) * size + "," + d.j * size + ")";
                })
                .each(plot);

            // Titles for the diagonal.
            cell.filter(function(d) {
                    return d.i === d.j;
                }).append("text")
                .attr("x", padding)
                .attr("y", padding)
                .attr("dy", ".71em")
                .text(function(d) {
                    return d.x;
                });

            cell.call(brush);

            function plot(p) {
                var cell = d3.select(this);

                x.domain(domainByTrait[p.x]);
                y.domain(domainByTrait[p.y]);

                cell.append("rect")
                    .attr("class", "frame")
                    .attr("x", padding / 2)
                    .attr("y", padding / 2)
                    .attr("width", size - padding)
                    .attr("height", size - padding);

                cell.selectAll("circle")
                    .data(data)
                    .enter().append("circle")
                    .attr("class", function(d, i) {
                        return d.class;
                    })
                    .attr("cx", function(d) {
                        return x(d[p.x]);
                    })
                    .attr("cy", function(d) {
                        return y(d[p.y]);
                    })
                    .attr("r", function(d) {
                        if (d.centroid == 1) {
                            return 10;
                        } else {
                            return 5;
                        }
                    })
                    .style("stroke", function(d) {
                        if (d.centroid == 1) {
                            return "black";
                        } else {
                            return "none";
                        }
                    })
                    .style("stroke-width", 3)
                    .style("opacity", function(d) {
                        if (d.centroid == 1) {
                            return 1.0;
                        } else {
                            return opacityCircles;
                        }
                    })
                    .style("fill", function(d) {
                        if (d.centroid == 1) {
                            return d3.schemeCategory10[d.class];
                        } else {
                            return d3.schemeCategory10[d.class];
                        }
                    })
                    .style("z-index", function(d) {
                        if (d.centroid == 1) {
                            return 1000;
                        }
                    });
                //.on("mouseover", showTooltip)
                //.on("mouseout",  removeTooltip);
            }


            var brushCell;

            // Clear the previously-active brush, if any.
            function brushstart(p) {
                if (brushCell !== this) {
                    d3.select(brushCell).call(brush.move, null);
                    brushCell = this;
                    x.domain(domainByTrait[p.x]);
                    y.domain(domainByTrait[p.y]);
                }
            }

            // Highlight the selected circles.
            function brushmove(p) {
                var e = d3.brushSelection(this);
                svg.selectAll("circle").classed("hidden", function(d) {
                    return !e ?
                        false :
                        (
                            e[0][0] > x(+d[p.x]) || x(+d[p.x]) > e[1][0] ||
                            e[0][1] > y(+d[p.y]) || y(+d[p.y]) > e[1][1]
                        );
                });
            }

            // If the brush is empty, select all circles.
            function brushend() {
                var e = d3.brushSelection(this);
                if (e === null) svg.selectAll(".hidden").classed("hidden", false);
            }

        });

        $('#table-responsive1').hide(500);
        $('#card2').addClass("disabled-everything");
        $('#card3').removeClass("disabled-everything");
        $('#downloadresult').attr("href", "./media/"+uploadedfileName);
        $('#outgraph').removeAttr("hidden");
        $('.accordion').removeAttr("hidden");
        $('#table-responsive2').removeAttr("hidden");
    });

    $(".js-upload").click(function() {
        $("#fileupload").click();
    });

    $('body').on('click', 'button.attribute-btn', function() {

        var value = $(this).val();
        if ($.inArray(value, chosenAttr) == -1) {
            $(this).removeClass("btn-outline-danger");
            $(this).addClass("btn-outline-success");
            chosenAttr.push(value);
            clickCounter++;
        } else {
            $(this).removeClass("btn-outline-success");
            $(this).addClass("btn-outline-danger");
            chosenAttr.splice($.inArray(value, chosenAttr), 1);
            clickCounter--;
        }

        if (clickCounter > 1) {
            $('#inputs').removeAttr("disabled");
        } else {
            $('#inputs').attr("disabled", true);
        }
    });

    $("#fileupload").fileupload({
        dataType: 'json',
        done: function(e, data) {
            if (data.result.is_valid) {
                uploadedfileName = data.result.name;
                uid = data.result.uid;
                console.log(uid);
                $.post("./csvreader", {
                    filename: uploadedfileName,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                }, function(data, status) {
                    var result_table_data = '';
                    var header = 1;

                    $.each(data, function(key, value) {
                        if (header == 1) {
                            result_table_data += '<thead><tr>'
                            $.each(data[key], function(objkey, objvalue) {
                                result_table_data += '<th scope="col"><button class="btn btn-outline-danger attribute-btn" value=' + objkey + '>' + objkey + '</button></th>'
                            });
                            result_table_data += '</tr></thead><tbody>'
                            header = 0;
                        } else {
                            result_table_data += '<tr>'
                            $.each(data[key], function(objkey, objvalue) {
                                result_table_data += '<td>' + objvalue + '</td>'
                            });
                            result_table_data += '</tr>'
                        }
                        if (key == 10) {
                            return false;
                        }
                    });
                    result_table_data += '</tbody>'

                    $('#sample-table').append(result_table_data);
                    $('#table-responsive1').removeAttr("hidden");
                    $('#card2').removeClass("disabled-everything");
                    $('#card1').addClass("disabled-everything");
                });
            }
        }
    });
});
