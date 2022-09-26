
"use strict";

let Polygon2D = require('./Polygon2D.js');
let PointCloudWithPose = require('./PointCloudWithPose.js');
let PolygonWithHolesStamped = require('./PolygonWithHolesStamped.js');
let Point2D = require('./Point2D.js');
let PolygonWithHoles = require('./PolygonWithHoles.js');
let PolynomialSegment = require('./PolynomialSegment.js');
let PolynomialTrajectory = require('./PolynomialTrajectory.js');
let PolynomialTrajectory4D = require('./PolynomialTrajectory4D.js');
let PolynomialSegment4D = require('./PolynomialSegment4D.js');

module.exports = {
  Polygon2D: Polygon2D,
  PointCloudWithPose: PointCloudWithPose,
  PolygonWithHolesStamped: PolygonWithHolesStamped,
  Point2D: Point2D,
  PolygonWithHoles: PolygonWithHoles,
  PolynomialSegment: PolynomialSegment,
  PolynomialTrajectory: PolynomialTrajectory,
  PolynomialTrajectory4D: PolynomialTrajectory4D,
  PolynomialSegment4D: PolynomialSegment4D,
};
