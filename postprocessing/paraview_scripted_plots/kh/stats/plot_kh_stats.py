# trace generated using paraview version 5.6.1
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# set active view
SetActiveView(None)

CreateLayout('Layout #1')

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1216, 799]
renderView1.AnnotationColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
renderView1.StereoType = 0
renderView1.Background = [1.0, 1.0, 1.0]
renderView1.OSPRayMaterialLibrary = materialLibrary1

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView1.AxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
renderView1.AxesGrid.XTitleFontFile = ''
renderView1.AxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
renderView1.AxesGrid.YTitleFontFile = ''
renderView1.AxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
renderView1.AxesGrid.ZTitleFontFile = ''
renderView1.AxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
renderView1.AxesGrid.XLabelFontFile = ''
renderView1.AxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
renderView1.AxesGrid.YLabelFontFile = ''
renderView1.AxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
renderView1.AxesGrid.ZLabelFontFile = ''

# get layout
layout1 = GetLayout()

# place view in the layout
layout1.AssignView(0, renderView1)

# create a new 'NetCDF Reader'
kh_mean_1nc = NetCDFReader(FileName=['/scratch/snx3000/klye/kh_tube_3d_stats/3druns_s839/3drunscloud/kelvinhelmholtz_3d_tube/stats/kelvinhelmholtz_64_0.1/kh_mean_1.nc'])
kh_mean_1nc.Dimensions = '(x, y, z)'

# show data in view
kh_mean_1ncDisplay = Show(kh_mean_1nc, renderView1)

# trace defaults for the display properties.
kh_mean_1ncDisplay.Representation = 'Outline'
kh_mean_1ncDisplay.ColorArrayName = [None, '']
kh_mean_1ncDisplay.OSPRayScaleArray = 'E'
kh_mean_1ncDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
kh_mean_1ncDisplay.SelectOrientationVectors = 'E'
kh_mean_1ncDisplay.ScaleFactor = 6.300000000000001
kh_mean_1ncDisplay.SelectScaleArray = 'E'
kh_mean_1ncDisplay.GlyphType = 'Arrow'
kh_mean_1ncDisplay.GlyphTableIndexArray = 'E'
kh_mean_1ncDisplay.GaussianRadius = 0.315
kh_mean_1ncDisplay.SetScaleArray = ['POINTS', 'E']
kh_mean_1ncDisplay.ScaleTransferFunction = 'PiecewiseFunction'
kh_mean_1ncDisplay.OpacityArray = ['POINTS', 'E']
kh_mean_1ncDisplay.OpacityTransferFunction = 'PiecewiseFunction'
kh_mean_1ncDisplay.DataAxesGrid = 'GridAxesRepresentation'
kh_mean_1ncDisplay.SelectionCellLabelFontFile = ''
kh_mean_1ncDisplay.SelectionPointLabelFontFile = ''
kh_mean_1ncDisplay.PolarAxes = 'PolarAxesRepresentation'
kh_mean_1ncDisplay.ScalarOpacityUnitDistance = 1.7320508075688774
kh_mean_1ncDisplay.Slice = 31

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
kh_mean_1ncDisplay.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1ncDisplay.DataAxesGrid.XTitleFontFile = ''
kh_mean_1ncDisplay.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1ncDisplay.DataAxesGrid.YTitleFontFile = ''
kh_mean_1ncDisplay.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1ncDisplay.DataAxesGrid.ZTitleFontFile = ''
kh_mean_1ncDisplay.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1ncDisplay.DataAxesGrid.XLabelFontFile = ''
kh_mean_1ncDisplay.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1ncDisplay.DataAxesGrid.YLabelFontFile = ''
kh_mean_1ncDisplay.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1ncDisplay.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
kh_mean_1ncDisplay.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1ncDisplay.PolarAxes.PolarAxisTitleFontFile = ''
kh_mean_1ncDisplay.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1ncDisplay.PolarAxes.PolarAxisLabelFontFile = ''
kh_mean_1ncDisplay.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1ncDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
kh_mean_1ncDisplay.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1ncDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(kh_mean_1ncDisplay, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
kh_mean_1ncDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
kh_mean_1ncDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'rho'
rhoLUT = GetColorTransferFunction('rho')
rhoLUT.RGBPoints = [0.9988457587084298, 0.231373, 0.298039, 0.752941, 1.5097528826305058, 0.865003, 0.865003, 0.865003, 2.0206600065525815, 0.705882, 0.0156863, 0.14902]
rhoLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'rho'
rhoPWF = GetOpacityTransferFunction('rho')
rhoPWF.Points = [0.9988457587084298, 0.0, 0.5, 0.0, 2.0206600065525815, 1.0, 0.5, 0.0]
rhoPWF.ScalarRangeInitialized = 1

# change representation type
kh_mean_1ncDisplay.SetRepresentationType('Volume')

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
rhoLUT.ApplyPreset('Viridis (matplotlib)', True)

# Rescale transfer function
rhoLUT.RescaleTransferFunction(1.1, 2.15)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(1.1, 2.15)

# current camera placement for renderView1
renderView1.CameraPosition = [179.77574194433058, 165.80771954174702, 97.93244529653035]
renderView1.CameraFocalPoint = [31.5, 31.499999999999996, 31.499999999999993]
renderView1.CameraViewUp = [-0.374632539508766, 0.7090754646792181, -0.5973796495790294]
renderView1.CameraParallelScale = 54.559600438419636

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/kh/stats/kh_mean_64_1.png', renderView1, ImageResolution=[3840, 2160])

# create a new 'NetCDF Reader'
kh_mean_1nc_1 = NetCDFReader(FileName=['/scratch/snx3000/klye/kh_tube_3d_stats/3druns_s839/3drunscloud/kelvinhelmholtz_3d_tube/stats/kelvinhelmholtz_128_0.1/kh_mean_1.nc'])
kh_mean_1nc_1.Dimensions = '(x, y, z)'

# hide data in view
Hide(kh_mean_1nc, renderView1)

# show data in view
kh_mean_1nc_1Display = Show(kh_mean_1nc_1, renderView1)

# trace defaults for the display properties.
kh_mean_1nc_1Display.Representation = 'Outline'
kh_mean_1nc_1Display.ColorArrayName = [None, '']
kh_mean_1nc_1Display.OSPRayScaleArray = 'E'
kh_mean_1nc_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
kh_mean_1nc_1Display.SelectOrientationVectors = 'E'
kh_mean_1nc_1Display.ScaleFactor = 12.700000000000001
kh_mean_1nc_1Display.SelectScaleArray = 'E'
kh_mean_1nc_1Display.GlyphType = 'Arrow'
kh_mean_1nc_1Display.GlyphTableIndexArray = 'E'
kh_mean_1nc_1Display.GaussianRadius = 0.635
kh_mean_1nc_1Display.SetScaleArray = ['POINTS', 'E']
kh_mean_1nc_1Display.ScaleTransferFunction = 'PiecewiseFunction'
kh_mean_1nc_1Display.OpacityArray = ['POINTS', 'E']
kh_mean_1nc_1Display.OpacityTransferFunction = 'PiecewiseFunction'
kh_mean_1nc_1Display.DataAxesGrid = 'GridAxesRepresentation'
kh_mean_1nc_1Display.SelectionCellLabelFontFile = ''
kh_mean_1nc_1Display.SelectionPointLabelFontFile = ''
kh_mean_1nc_1Display.PolarAxes = 'PolarAxesRepresentation'
kh_mean_1nc_1Display.ScalarOpacityUnitDistance = 1.732050807568877
kh_mean_1nc_1Display.Slice = 63

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
kh_mean_1nc_1Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1nc_1Display.DataAxesGrid.XTitleFontFile = ''
kh_mean_1nc_1Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1nc_1Display.DataAxesGrid.YTitleFontFile = ''
kh_mean_1nc_1Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1nc_1Display.DataAxesGrid.ZTitleFontFile = ''
kh_mean_1nc_1Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1nc_1Display.DataAxesGrid.XLabelFontFile = ''
kh_mean_1nc_1Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1nc_1Display.DataAxesGrid.YLabelFontFile = ''
kh_mean_1nc_1Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1nc_1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
kh_mean_1nc_1Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1nc_1Display.PolarAxes.PolarAxisTitleFontFile = ''
kh_mean_1nc_1Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1nc_1Display.PolarAxes.PolarAxisLabelFontFile = ''
kh_mean_1nc_1Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1nc_1Display.PolarAxes.LastRadialAxisTextFontFile = ''
kh_mean_1nc_1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1nc_1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(kh_mean_1nc_1Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
kh_mean_1nc_1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
kh_mean_1nc_1Display.SetScalarBarVisibility(renderView1, True)

# change representation type
kh_mean_1nc_1Display.SetRepresentationType('Volume')

# Rescale transfer function
rhoLUT.RescaleTransferFunction(1.1, 2.15)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(1.1, 2.15)

# current camera placement for renderView1
renderView1.CameraPosition = [362.4050670941262, 334.24730764764826, 197.41937385173551]
renderView1.CameraFocalPoint = [63.5, 63.5, 63.5]
renderView1.CameraViewUp = [-0.374632539508766, 0.7090754646792181, -0.5973796495790294]
renderView1.CameraParallelScale = 109.9852262806237

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/kh/stats/kh_mean_128_1.png', renderView1, ImageResolution=[3840, 2160])

# hide data in view
Hide(kh_mean_1nc_1, renderView1)

# create a new 'NetCDF Reader'
kh_mean_1nc_2 = NetCDFReader(FileName=['/scratch/snx3000/klye/kh_tube_3d_stats/3druns_s839/3drunscloud/kelvinhelmholtz_3d_tube/stats/kelvinhelmholtz_256_0.1/kh_mean_1.nc'])
kh_mean_1nc_2.Dimensions = '(x, y, z)'

# show data in view
kh_mean_1nc_2Display = Show(kh_mean_1nc_2, renderView1)

# trace defaults for the display properties.
kh_mean_1nc_2Display.Representation = 'Outline'
kh_mean_1nc_2Display.ColorArrayName = [None, '']
kh_mean_1nc_2Display.OSPRayScaleArray = 'E'
kh_mean_1nc_2Display.OSPRayScaleFunction = 'PiecewiseFunction'
kh_mean_1nc_2Display.SelectOrientationVectors = 'E'
kh_mean_1nc_2Display.ScaleFactor = 25.5
kh_mean_1nc_2Display.SelectScaleArray = 'E'
kh_mean_1nc_2Display.GlyphType = 'Arrow'
kh_mean_1nc_2Display.GlyphTableIndexArray = 'E'
kh_mean_1nc_2Display.GaussianRadius = 1.2750000000000001
kh_mean_1nc_2Display.SetScaleArray = ['POINTS', 'E']
kh_mean_1nc_2Display.ScaleTransferFunction = 'PiecewiseFunction'
kh_mean_1nc_2Display.OpacityArray = ['POINTS', 'E']
kh_mean_1nc_2Display.OpacityTransferFunction = 'PiecewiseFunction'
kh_mean_1nc_2Display.DataAxesGrid = 'GridAxesRepresentation'
kh_mean_1nc_2Display.SelectionCellLabelFontFile = ''
kh_mean_1nc_2Display.SelectionPointLabelFontFile = ''
kh_mean_1nc_2Display.PolarAxes = 'PolarAxesRepresentation'
kh_mean_1nc_2Display.ScalarOpacityUnitDistance = 1.7320508075688774
kh_mean_1nc_2Display.Slice = 127

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
kh_mean_1nc_2Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1nc_2Display.DataAxesGrid.XTitleFontFile = ''
kh_mean_1nc_2Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1nc_2Display.DataAxesGrid.YTitleFontFile = ''
kh_mean_1nc_2Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1nc_2Display.DataAxesGrid.ZTitleFontFile = ''
kh_mean_1nc_2Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1nc_2Display.DataAxesGrid.XLabelFontFile = ''
kh_mean_1nc_2Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1nc_2Display.DataAxesGrid.YLabelFontFile = ''
kh_mean_1nc_2Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1nc_2Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
kh_mean_1nc_2Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1nc_2Display.PolarAxes.PolarAxisTitleFontFile = ''
kh_mean_1nc_2Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1nc_2Display.PolarAxes.PolarAxisLabelFontFile = ''
kh_mean_1nc_2Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1nc_2Display.PolarAxes.LastRadialAxisTextFontFile = ''
kh_mean_1nc_2Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1nc_2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(kh_mean_1nc_2Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
kh_mean_1nc_2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
kh_mean_1nc_2Display.SetScalarBarVisibility(renderView1, True)

# change representation type
kh_mean_1nc_2Display.SetRepresentationType('Volume')

# Rescale transfer function
rhoLUT.RescaleTransferFunction(1.1, 2.15)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(1.1, 2.15)

# current camera placement for renderView1
renderView1.CameraPosition = [727.663717393718, 671.1264838594512, 396.39323096214616]
renderView1.CameraFocalPoint = [127.5, 127.5, 127.5]
renderView1.CameraViewUp = [-0.374632539508766, 0.7090754646792181, -0.5973796495790294]
renderView1.CameraParallelScale = 220.83647796503186

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/kh/stats/kh_mean_256_1.png', renderView1, ImageResolution=[3840, 2160])

# create a new 'NetCDF Reader'
kh_mean_1nc_3 = NetCDFReader(FileName=['/scratch/snx3000/klye/kh_tube_3d_stats/3druns_s839/3drunscloud/kelvinhelmholtz_3d_tube/stats/kelvinhelmholtz_256_0.1/kh_mean_1.nc'])
kh_mean_1nc_3.Dimensions = '(x, y, z)'

# hide data in view
Hide(kh_mean_1nc_2, renderView1)

# set active source
SetActiveSource(kh_mean_1nc_3)

# show data in view
kh_mean_1nc_3Display = Show(kh_mean_1nc_3, renderView1)

# trace defaults for the display properties.
kh_mean_1nc_3Display.Representation = 'Outline'
kh_mean_1nc_3Display.ColorArrayName = [None, '']
kh_mean_1nc_3Display.OSPRayScaleArray = 'E'
kh_mean_1nc_3Display.OSPRayScaleFunction = 'PiecewiseFunction'
kh_mean_1nc_3Display.SelectOrientationVectors = 'E'
kh_mean_1nc_3Display.ScaleFactor = 25.5
kh_mean_1nc_3Display.SelectScaleArray = 'E'
kh_mean_1nc_3Display.GlyphType = 'Arrow'
kh_mean_1nc_3Display.GlyphTableIndexArray = 'E'
kh_mean_1nc_3Display.GaussianRadius = 1.2750000000000001
kh_mean_1nc_3Display.SetScaleArray = ['POINTS', 'E']
kh_mean_1nc_3Display.ScaleTransferFunction = 'PiecewiseFunction'
kh_mean_1nc_3Display.OpacityArray = ['POINTS', 'E']
kh_mean_1nc_3Display.OpacityTransferFunction = 'PiecewiseFunction'
kh_mean_1nc_3Display.DataAxesGrid = 'GridAxesRepresentation'
kh_mean_1nc_3Display.SelectionCellLabelFontFile = ''
kh_mean_1nc_3Display.SelectionPointLabelFontFile = ''
kh_mean_1nc_3Display.PolarAxes = 'PolarAxesRepresentation'
kh_mean_1nc_3Display.ScalarOpacityUnitDistance = 1.7320508075688774
kh_mean_1nc_3Display.Slice = 127

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
kh_mean_1nc_3Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1nc_3Display.DataAxesGrid.XTitleFontFile = ''
kh_mean_1nc_3Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1nc_3Display.DataAxesGrid.YTitleFontFile = ''
kh_mean_1nc_3Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1nc_3Display.DataAxesGrid.ZTitleFontFile = ''
kh_mean_1nc_3Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1nc_3Display.DataAxesGrid.XLabelFontFile = ''
kh_mean_1nc_3Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1nc_3Display.DataAxesGrid.YLabelFontFile = ''
kh_mean_1nc_3Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1nc_3Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
kh_mean_1nc_3Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1nc_3Display.PolarAxes.PolarAxisTitleFontFile = ''
kh_mean_1nc_3Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1nc_3Display.PolarAxes.PolarAxisLabelFontFile = ''
kh_mean_1nc_3Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1nc_3Display.PolarAxes.LastRadialAxisTextFontFile = ''
kh_mean_1nc_3Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1nc_3Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# set scalar coloring
ColorBy(kh_mean_1nc_3Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
kh_mean_1nc_3Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
kh_mean_1nc_3Display.SetScalarBarVisibility(renderView1, True)

# change representation type
kh_mean_1nc_3Display.SetRepresentationType('Volume')

# Rescale transfer function
rhoLUT.RescaleTransferFunction(1.1, 2.15)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(1.1, 2.15)

# current camera placement for renderView1
renderView1.CameraPosition = [727.663717393718, 671.1264838594512, 396.39323096214616]
renderView1.CameraFocalPoint = [127.5, 127.5, 127.5]
renderView1.CameraViewUp = [-0.374632539508766, 0.7090754646792181, -0.5973796495790294]
renderView1.CameraParallelScale = 220.83647796503186

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/kh/stats/kh_mean_256_1.png', renderView1, ImageResolution=[3840, 2160])

# hide data in view
Hide(kh_mean_1nc_3, renderView1)

# create a new 'NetCDF Reader'
kh_mean_1hdf5 = NetCDFReader(FileName=['/scratch/snx3000/klye/kh_tube_3d_stats/3druns_s839/3drunscloud/kelvinhelmholtz_3d_tube/stats/kelvinhelmholtz_512_0.01/kh_mean_1.hdf5'])
kh_mean_1hdf5.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# destroy kh_mean_1hdf5
Delete(kh_mean_1hdf5)
del kh_mean_1hdf5

# create a new 'NetCDF Reader'
kh_mean_1hdf5 = NetCDFReader(FileName=['/scratch/snx3000/klye/kh_tube_3d_stats/3druns_s839/3drunscloud/kelvinhelmholtz_3d_tube/stats/kelvinhelmholtz_512_0.1/kh_mean_1.hdf5'])
kh_mean_1hdf5.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# show data in view
kh_mean_1nc_3Display = Show(kh_mean_1nc_3, renderView1)

# reset view to fit data
renderView1.ResetCamera()

# show color bar/color legend
kh_mean_1nc_3Display.SetScalarBarVisibility(renderView1, True)

# show data in view
kh_mean_1hdf5Display = Show(kh_mean_1hdf5, renderView1)

# trace defaults for the display properties.
kh_mean_1hdf5Display.Representation = 'Outline'
kh_mean_1hdf5Display.ColorArrayName = [None, '']
kh_mean_1hdf5Display.OSPRayScaleArray = 'E'
kh_mean_1hdf5Display.OSPRayScaleFunction = 'PiecewiseFunction'
kh_mean_1hdf5Display.SelectOrientationVectors = 'E'
kh_mean_1hdf5Display.ScaleFactor = 51.1
kh_mean_1hdf5Display.SelectScaleArray = 'E'
kh_mean_1hdf5Display.GlyphType = 'Arrow'
kh_mean_1hdf5Display.GlyphTableIndexArray = 'E'
kh_mean_1hdf5Display.GaussianRadius = 2.555
kh_mean_1hdf5Display.SetScaleArray = ['POINTS', 'E']
kh_mean_1hdf5Display.ScaleTransferFunction = 'PiecewiseFunction'
kh_mean_1hdf5Display.OpacityArray = ['POINTS', 'E']
kh_mean_1hdf5Display.OpacityTransferFunction = 'PiecewiseFunction'
kh_mean_1hdf5Display.DataAxesGrid = 'GridAxesRepresentation'
kh_mean_1hdf5Display.SelectionCellLabelFontFile = ''
kh_mean_1hdf5Display.SelectionPointLabelFontFile = ''
kh_mean_1hdf5Display.PolarAxes = 'PolarAxesRepresentation'
kh_mean_1hdf5Display.ScalarOpacityUnitDistance = 1.732050807568877
kh_mean_1hdf5Display.Slice = 255

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
kh_mean_1hdf5Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1hdf5Display.DataAxesGrid.XTitleFontFile = ''
kh_mean_1hdf5Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1hdf5Display.DataAxesGrid.YTitleFontFile = ''
kh_mean_1hdf5Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1hdf5Display.DataAxesGrid.ZTitleFontFile = ''
kh_mean_1hdf5Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1hdf5Display.DataAxesGrid.XLabelFontFile = ''
kh_mean_1hdf5Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1hdf5Display.DataAxesGrid.YLabelFontFile = ''
kh_mean_1hdf5Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1hdf5Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
kh_mean_1hdf5Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1hdf5Display.PolarAxes.PolarAxisTitleFontFile = ''
kh_mean_1hdf5Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1hdf5Display.PolarAxes.PolarAxisLabelFontFile = ''
kh_mean_1hdf5Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1hdf5Display.PolarAxes.LastRadialAxisTextFontFile = ''
kh_mean_1hdf5Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_1hdf5Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# update the view to ensure updated data information
renderView1.Update()

# Rescale transfer function
rhoLUT.RescaleTransferFunction(0.996205717856, 2.15)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(0.996205717856, 2.15)

# hide data in view
Hide(kh_mean_1nc_3, renderView1)

# set scalar coloring
ColorBy(kh_mean_1hdf5Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
kh_mean_1hdf5Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
kh_mean_1hdf5Display.SetScalarBarVisibility(renderView1, True)

# change representation type
kh_mean_1hdf5Display.SetRepresentationType('Volume')

# set active source
SetActiveSource(kh_mean_1nc_3)

# Rescale transfer function
rhoLUT.RescaleTransferFunction(1.1, 2.15)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(1.1, 2.15)

# current camera placement for renderView1
renderView1.CameraPosition = [1684.170116815544, 1537.5270936211268, 824.9397903799947]
renderView1.CameraFocalPoint = [127.5, 127.5, 127.5]
renderView1.CameraViewUp = [-0.374632539508766, 0.7090754646792181, -0.5973796495790294]
renderView1.CameraParallelScale = 220.83647796503186

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/kh/stats/kh_mean_512_1.png', renderView1, ImageResolution=[3840, 2160])

# hide data in view
Hide(kh_mean_1hdf5, renderView1)

# set active source
SetActiveSource(kh_mean_1nc)

# destroy kh_mean_1nc
Delete(kh_mean_1nc)
del kh_mean_1nc

# set active source
SetActiveSource(kh_mean_1nc_1)

# destroy kh_mean_1nc_1
Delete(kh_mean_1nc_1)
del kh_mean_1nc_1

# set active source
SetActiveSource(kh_mean_1nc_3)

# destroy kh_mean_1nc_3
Delete(kh_mean_1nc_3)
del kh_mean_1nc_3

# set active source
SetActiveSource(kh_mean_1nc_2)

# destroy kh_mean_1nc_2
Delete(kh_mean_1nc_2)
del kh_mean_1nc_2

# set active source
SetActiveSource(kh_mean_1hdf5)

# destroy kh_mean_1hdf5
Delete(kh_mean_1hdf5)
del kh_mean_1hdf5

# create a new 'NetCDF Reader'
kh_variance_1hdf5 = NetCDFReader(FileName=['/scratch/snx3000/klye/kh_tube_3d_stats/3druns_s839/3drunscloud/kelvinhelmholtz_3d_tube/stats/kelvinhelmholtz_64_0.1/kh_variance_1.hdf5'])
kh_variance_1hdf5.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# show data in view
kh_variance_1hdf5Display = Show(kh_variance_1hdf5, renderView1)

# trace defaults for the display properties.
kh_variance_1hdf5Display.Representation = 'Outline'
kh_variance_1hdf5Display.ColorArrayName = [None, '']
kh_variance_1hdf5Display.OSPRayScaleArray = 'E'
kh_variance_1hdf5Display.OSPRayScaleFunction = 'PiecewiseFunction'
kh_variance_1hdf5Display.SelectOrientationVectors = 'E'
kh_variance_1hdf5Display.ScaleFactor = 6.300000000000001
kh_variance_1hdf5Display.SelectScaleArray = 'E'
kh_variance_1hdf5Display.GlyphType = 'Arrow'
kh_variance_1hdf5Display.GlyphTableIndexArray = 'E'
kh_variance_1hdf5Display.GaussianRadius = 0.315
kh_variance_1hdf5Display.SetScaleArray = ['POINTS', 'E']
kh_variance_1hdf5Display.ScaleTransferFunction = 'PiecewiseFunction'
kh_variance_1hdf5Display.OpacityArray = ['POINTS', 'E']
kh_variance_1hdf5Display.OpacityTransferFunction = 'PiecewiseFunction'
kh_variance_1hdf5Display.DataAxesGrid = 'GridAxesRepresentation'
kh_variance_1hdf5Display.SelectionCellLabelFontFile = ''
kh_variance_1hdf5Display.SelectionPointLabelFontFile = ''
kh_variance_1hdf5Display.PolarAxes = 'PolarAxesRepresentation'
kh_variance_1hdf5Display.ScalarOpacityUnitDistance = 1.7320508075688774
kh_variance_1hdf5Display.Slice = 31

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
kh_variance_1hdf5Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_1hdf5Display.DataAxesGrid.XTitleFontFile = ''
kh_variance_1hdf5Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_1hdf5Display.DataAxesGrid.YTitleFontFile = ''
kh_variance_1hdf5Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_1hdf5Display.DataAxesGrid.ZTitleFontFile = ''
kh_variance_1hdf5Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_1hdf5Display.DataAxesGrid.XLabelFontFile = ''
kh_variance_1hdf5Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_1hdf5Display.DataAxesGrid.YLabelFontFile = ''
kh_variance_1hdf5Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_1hdf5Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
kh_variance_1hdf5Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_1hdf5Display.PolarAxes.PolarAxisTitleFontFile = ''
kh_variance_1hdf5Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_1hdf5Display.PolarAxes.PolarAxisLabelFontFile = ''
kh_variance_1hdf5Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_1hdf5Display.PolarAxes.LastRadialAxisTextFontFile = ''
kh_variance_1hdf5Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_1hdf5Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(kh_variance_1hdf5Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
kh_variance_1hdf5Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
kh_variance_1hdf5Display.SetScalarBarVisibility(renderView1, True)

# change representation type
kh_variance_1hdf5Display.SetRepresentationType('Volume')

# rescale color and/or opacity maps used to exactly fit the current data range
kh_variance_1hdf5Display.RescaleTransferFunctionToDataRange(False, True)

# current camera placement for renderView1
renderView1.CameraPosition = [179.77574194433032, 165.8077195417468, 97.93244529653022]
renderView1.CameraFocalPoint = [31.5, 31.5, 31.5]
renderView1.CameraViewUp = [-0.374632539508766, 0.7090754646792181, -0.5973796495790294]
renderView1.CameraParallelScale = 54.559600438419636

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/kh/stats/kh_variance_64_1.png', renderView1, ImageResolution=[3840, 2160])

# get color legend/bar for rhoLUT in view renderView1
rhoLUTColorBar = GetScalarBar(rhoLUT, renderView1)
rhoLUTColorBar.Title = 'rho'
rhoLUTColorBar.ComponentTitle = ''
rhoLUTColorBar.TitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
rhoLUTColorBar.TitleFontFile = ''
rhoLUTColorBar.LabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
rhoLUTColorBar.LabelFontFile = ''

# Properties modified on rhoLUTColorBar
rhoLUTColorBar.Title = '$\\varrho$'
rhoLUTColorBar.HorizontalTitle = 1
rhoLUTColorBar.RangeLabelFormat = '%-#6.1f'

# current camera placement for renderView1
renderView1.CameraPosition = [179.77574194433032, 165.8077195417468, 97.93244529653022]
renderView1.CameraFocalPoint = [31.5, 31.5, 31.5]
renderView1.CameraViewUp = [-0.374632539508766, 0.7090754646792181, -0.5973796495790294]
renderView1.CameraParallelScale = 54.559600438419636

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/kh/stats/kh_variance_64_1.png', renderView1, ImageResolution=[3840, 2160])

# hide data in view
Hide(kh_variance_1hdf5, renderView1)

# create a new 'NetCDF Reader'
kh_variance_1hdf5_1 = NetCDFReader(FileName=['/scratch/snx3000/klye/kh_tube_3d_stats/3druns_s839/3drunscloud/kelvinhelmholtz_3d_tube/stats/kelvinhelmholtz_128_0.1/kh_variance_1.hdf5'])
kh_variance_1hdf5_1.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# show data in view
kh_variance_1hdf5_1Display = Show(kh_variance_1hdf5_1, renderView1)

# trace defaults for the display properties.
kh_variance_1hdf5_1Display.Representation = 'Outline'
kh_variance_1hdf5_1Display.ColorArrayName = [None, '']
kh_variance_1hdf5_1Display.OSPRayScaleArray = 'E'
kh_variance_1hdf5_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
kh_variance_1hdf5_1Display.SelectOrientationVectors = 'E'
kh_variance_1hdf5_1Display.ScaleFactor = 12.700000000000001
kh_variance_1hdf5_1Display.SelectScaleArray = 'E'
kh_variance_1hdf5_1Display.GlyphType = 'Arrow'
kh_variance_1hdf5_1Display.GlyphTableIndexArray = 'E'
kh_variance_1hdf5_1Display.GaussianRadius = 0.635
kh_variance_1hdf5_1Display.SetScaleArray = ['POINTS', 'E']
kh_variance_1hdf5_1Display.ScaleTransferFunction = 'PiecewiseFunction'
kh_variance_1hdf5_1Display.OpacityArray = ['POINTS', 'E']
kh_variance_1hdf5_1Display.OpacityTransferFunction = 'PiecewiseFunction'
kh_variance_1hdf5_1Display.DataAxesGrid = 'GridAxesRepresentation'
kh_variance_1hdf5_1Display.SelectionCellLabelFontFile = ''
kh_variance_1hdf5_1Display.SelectionPointLabelFontFile = ''
kh_variance_1hdf5_1Display.PolarAxes = 'PolarAxesRepresentation'
kh_variance_1hdf5_1Display.ScalarOpacityUnitDistance = 1.732050807568877
kh_variance_1hdf5_1Display.Slice = 63

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
kh_variance_1hdf5_1Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_1hdf5_1Display.DataAxesGrid.XTitleFontFile = ''
kh_variance_1hdf5_1Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_1hdf5_1Display.DataAxesGrid.YTitleFontFile = ''
kh_variance_1hdf5_1Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_1hdf5_1Display.DataAxesGrid.ZTitleFontFile = ''
kh_variance_1hdf5_1Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_1hdf5_1Display.DataAxesGrid.XLabelFontFile = ''
kh_variance_1hdf5_1Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_1hdf5_1Display.DataAxesGrid.YLabelFontFile = ''
kh_variance_1hdf5_1Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_1hdf5_1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
kh_variance_1hdf5_1Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_1hdf5_1Display.PolarAxes.PolarAxisTitleFontFile = ''
kh_variance_1hdf5_1Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_1hdf5_1Display.PolarAxes.PolarAxisLabelFontFile = ''
kh_variance_1hdf5_1Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_1hdf5_1Display.PolarAxes.LastRadialAxisTextFontFile = ''
kh_variance_1hdf5_1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_1hdf5_1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(kh_variance_1hdf5_1Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
kh_variance_1hdf5_1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
kh_variance_1hdf5_1Display.SetScalarBarVisibility(renderView1, True)

# change representation type
kh_variance_1hdf5_1Display.SetRepresentationType('Volume')

# Rescale transfer function
rhoLUT.RescaleTransferFunction(0.0, 0.17)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(0.0, 0.17)

# current camera placement for renderView1
renderView1.CameraPosition = [362.4050670941262, 334.24730764764826, 197.4193738517355]
renderView1.CameraFocalPoint = [63.5, 63.5, 63.5]
renderView1.CameraViewUp = [-0.374632539508766, 0.7090754646792181, -0.5973796495790294]
renderView1.CameraParallelScale = 109.9852262806237

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/kh/stats/kh_variance_128_1.png', renderView1, ImageResolution=[3840, 2160], 
    # PNG options
    CompressionLevel='0')

# hide data in view
Hide(kh_variance_1hdf5_1, renderView1)

# set active source
SetActiveSource(kh_variance_1hdf5)

# show data in view
kh_variance_1hdf5Display = Show(kh_variance_1hdf5, renderView1)

# show color bar/color legend
kh_variance_1hdf5Display.SetScalarBarVisibility(renderView1, True)

# reset view to fit data
renderView1.ResetCamera()

# current camera placement for renderView1
renderView1.CameraPosition = [179.77574194433035, 165.8077195417468, 97.9324452965302]
renderView1.CameraFocalPoint = [31.5, 31.5, 31.5]
renderView1.CameraViewUp = [-0.374632539508766, 0.7090754646792181, -0.5973796495790294]
renderView1.CameraParallelScale = 54.559600438419636

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/kh/stats/kh_variance_64_1.png', renderView1, ImageResolution=[3840, 2160])

# hide data in view
Hide(kh_variance_1hdf5, renderView1)

# create a new 'NetCDF Reader'
kh_variance_1hdf5_2 = NetCDFReader(FileName=['/scratch/snx3000/klye/kh_tube_3d_stats/3druns_s839/3drunscloud/kelvinhelmholtz_3d_tube/stats/kelvinhelmholtz_256_0.1/kh_variance_1.hdf5'])
kh_variance_1hdf5_2.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# show data in view
kh_variance_1hdf5_2Display = Show(kh_variance_1hdf5_2, renderView1)

# trace defaults for the display properties.
kh_variance_1hdf5_2Display.Representation = 'Outline'
kh_variance_1hdf5_2Display.ColorArrayName = [None, '']
kh_variance_1hdf5_2Display.OSPRayScaleArray = 'E'
kh_variance_1hdf5_2Display.OSPRayScaleFunction = 'PiecewiseFunction'
kh_variance_1hdf5_2Display.SelectOrientationVectors = 'E'
kh_variance_1hdf5_2Display.ScaleFactor = 25.5
kh_variance_1hdf5_2Display.SelectScaleArray = 'E'
kh_variance_1hdf5_2Display.GlyphType = 'Arrow'
kh_variance_1hdf5_2Display.GlyphTableIndexArray = 'E'
kh_variance_1hdf5_2Display.GaussianRadius = 1.2750000000000001
kh_variance_1hdf5_2Display.SetScaleArray = ['POINTS', 'E']
kh_variance_1hdf5_2Display.ScaleTransferFunction = 'PiecewiseFunction'
kh_variance_1hdf5_2Display.OpacityArray = ['POINTS', 'E']
kh_variance_1hdf5_2Display.OpacityTransferFunction = 'PiecewiseFunction'
kh_variance_1hdf5_2Display.DataAxesGrid = 'GridAxesRepresentation'
kh_variance_1hdf5_2Display.SelectionCellLabelFontFile = ''
kh_variance_1hdf5_2Display.SelectionPointLabelFontFile = ''
kh_variance_1hdf5_2Display.PolarAxes = 'PolarAxesRepresentation'
kh_variance_1hdf5_2Display.ScalarOpacityUnitDistance = 1.7320508075688774
kh_variance_1hdf5_2Display.Slice = 127

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
kh_variance_1hdf5_2Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_1hdf5_2Display.DataAxesGrid.XTitleFontFile = ''
kh_variance_1hdf5_2Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_1hdf5_2Display.DataAxesGrid.YTitleFontFile = ''
kh_variance_1hdf5_2Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_1hdf5_2Display.DataAxesGrid.ZTitleFontFile = ''
kh_variance_1hdf5_2Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_1hdf5_2Display.DataAxesGrid.XLabelFontFile = ''
kh_variance_1hdf5_2Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_1hdf5_2Display.DataAxesGrid.YLabelFontFile = ''
kh_variance_1hdf5_2Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_1hdf5_2Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
kh_variance_1hdf5_2Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_1hdf5_2Display.PolarAxes.PolarAxisTitleFontFile = ''
kh_variance_1hdf5_2Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_1hdf5_2Display.PolarAxes.PolarAxisLabelFontFile = ''
kh_variance_1hdf5_2Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_1hdf5_2Display.PolarAxes.LastRadialAxisTextFontFile = ''
kh_variance_1hdf5_2Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_1hdf5_2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(kh_variance_1hdf5_2Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
kh_variance_1hdf5_2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
kh_variance_1hdf5_2Display.SetScalarBarVisibility(renderView1, True)

# change representation type
kh_variance_1hdf5_2Display.SetRepresentationType('Volume')

# current camera placement for renderView1
renderView1.CameraPosition = [727.663717393718, 671.1264838594512, 396.39323096214605]
renderView1.CameraFocalPoint = [127.5, 127.5, 127.5]
renderView1.CameraViewUp = [-0.374632539508766, 0.7090754646792181, -0.5973796495790294]
renderView1.CameraParallelScale = 220.83647796503186

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/kh/stats/kh_variance_256_1.png', renderView1, ImageResolution=[3840, 2160], 
    # PNG options
    CompressionLevel='0')

# hide data in view
Hide(kh_variance_1hdf5_2, renderView1)

# create a new 'NetCDF Reader'
kh_variance_1hdf5_3 = NetCDFReader(FileName=['/scratch/snx3000/klye/kh_tube_3d_stats/3druns_s839/3drunscloud/kelvinhelmholtz_3d_tube/stats/kelvinhelmholtz_512_0.1/kh_variance_1.hdf5'])
kh_variance_1hdf5_3.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# show data in view
kh_variance_1hdf5_3Display = Show(kh_variance_1hdf5_3, renderView1)

# trace defaults for the display properties.
kh_variance_1hdf5_3Display.Representation = 'Outline'
kh_variance_1hdf5_3Display.ColorArrayName = [None, '']
kh_variance_1hdf5_3Display.OSPRayScaleArray = 'E'
kh_variance_1hdf5_3Display.OSPRayScaleFunction = 'PiecewiseFunction'
kh_variance_1hdf5_3Display.SelectOrientationVectors = 'E'
kh_variance_1hdf5_3Display.ScaleFactor = 51.1
kh_variance_1hdf5_3Display.SelectScaleArray = 'E'
kh_variance_1hdf5_3Display.GlyphType = 'Arrow'
kh_variance_1hdf5_3Display.GlyphTableIndexArray = 'E'
kh_variance_1hdf5_3Display.GaussianRadius = 2.555
kh_variance_1hdf5_3Display.SetScaleArray = ['POINTS', 'E']
kh_variance_1hdf5_3Display.ScaleTransferFunction = 'PiecewiseFunction'
kh_variance_1hdf5_3Display.OpacityArray = ['POINTS', 'E']
kh_variance_1hdf5_3Display.OpacityTransferFunction = 'PiecewiseFunction'
kh_variance_1hdf5_3Display.DataAxesGrid = 'GridAxesRepresentation'
kh_variance_1hdf5_3Display.SelectionCellLabelFontFile = ''
kh_variance_1hdf5_3Display.SelectionPointLabelFontFile = ''
kh_variance_1hdf5_3Display.PolarAxes = 'PolarAxesRepresentation'
kh_variance_1hdf5_3Display.ScalarOpacityUnitDistance = 1.732050807568877
kh_variance_1hdf5_3Display.Slice = 255

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
kh_variance_1hdf5_3Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_1hdf5_3Display.DataAxesGrid.XTitleFontFile = ''
kh_variance_1hdf5_3Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_1hdf5_3Display.DataAxesGrid.YTitleFontFile = ''
kh_variance_1hdf5_3Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_1hdf5_3Display.DataAxesGrid.ZTitleFontFile = ''
kh_variance_1hdf5_3Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_1hdf5_3Display.DataAxesGrid.XLabelFontFile = ''
kh_variance_1hdf5_3Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_1hdf5_3Display.DataAxesGrid.YLabelFontFile = ''
kh_variance_1hdf5_3Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_1hdf5_3Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
kh_variance_1hdf5_3Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_1hdf5_3Display.PolarAxes.PolarAxisTitleFontFile = ''
kh_variance_1hdf5_3Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_1hdf5_3Display.PolarAxes.PolarAxisLabelFontFile = ''
kh_variance_1hdf5_3Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_1hdf5_3Display.PolarAxes.LastRadialAxisTextFontFile = ''
kh_variance_1hdf5_3Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_1hdf5_3Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(kh_variance_1hdf5_3Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
kh_variance_1hdf5_3Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
kh_variance_1hdf5_3Display.SetScalarBarVisibility(renderView1, True)

# change representation type
kh_variance_1hdf5_3Display.SetRepresentationType('Volume')

# current camera placement for renderView1
renderView1.CameraPosition = [1458.1810179929016, 1344.884836283057, 794.3409451829672]
renderView1.CameraFocalPoint = [255.5, 255.5, 255.5]
renderView1.CameraViewUp = [-0.374632539508766, 0.7090754646792181, -0.5973796495790294]
renderView1.CameraParallelScale = 442.53898133384814

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/kh/stats/kh_variance_512_1.png', renderView1, ImageResolution=[3840, 2160], 
    # PNG options
    CompressionLevel='0')

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [1458.1810179929016, 1344.884836283057, 794.3409451829672]
renderView1.CameraFocalPoint = [255.5, 255.5, 255.5]
renderView1.CameraViewUp = [-0.374632539508766, 0.7090754646792181, -0.5973796495790294]
renderView1.CameraParallelScale = 442.53898133384814

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).