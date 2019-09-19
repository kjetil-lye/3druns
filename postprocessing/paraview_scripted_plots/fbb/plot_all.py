# trace generated using paraview version 5.6.2
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
renderView1.ViewSize = [1107, 799]
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
fbm_variance_1hdf5 = NetCDFReader(FileName=['/scratch/snx3000/klye/fbm/stats/H0_1/N512/fbm_variance_1.hdf5'])
fbm_variance_1hdf5.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# show data in view
fbm_variance_1hdf5Display = Show(fbm_variance_1hdf5, renderView1)

# trace defaults for the display properties.
fbm_variance_1hdf5Display.Representation = 'Outline'
fbm_variance_1hdf5Display.ColorArrayName = [None, '']
fbm_variance_1hdf5Display.OSPRayScaleArray = 'E'
fbm_variance_1hdf5Display.OSPRayScaleFunction = 'PiecewiseFunction'
fbm_variance_1hdf5Display.SelectOrientationVectors = 'E'
fbm_variance_1hdf5Display.ScaleFactor = 51.1
fbm_variance_1hdf5Display.SelectScaleArray = 'E'
fbm_variance_1hdf5Display.GlyphType = 'Arrow'
fbm_variance_1hdf5Display.GlyphTableIndexArray = 'E'
fbm_variance_1hdf5Display.GaussianRadius = 2.555
fbm_variance_1hdf5Display.SetScaleArray = ['POINTS', 'E']
fbm_variance_1hdf5Display.ScaleTransferFunction = 'PiecewiseFunction'
fbm_variance_1hdf5Display.OpacityArray = ['POINTS', 'E']
fbm_variance_1hdf5Display.OpacityTransferFunction = 'PiecewiseFunction'
fbm_variance_1hdf5Display.DataAxesGrid = 'GridAxesRepresentation'
fbm_variance_1hdf5Display.SelectionCellLabelFontFile = ''
fbm_variance_1hdf5Display.SelectionPointLabelFontFile = ''
fbm_variance_1hdf5Display.PolarAxes = 'PolarAxesRepresentation'
fbm_variance_1hdf5Display.ScalarOpacityUnitDistance = 1.732050807568877
fbm_variance_1hdf5Display.Slice = 255

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
fbm_variance_1hdf5Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5Display.DataAxesGrid.XTitleFontFile = ''
fbm_variance_1hdf5Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5Display.DataAxesGrid.YTitleFontFile = ''
fbm_variance_1hdf5Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5Display.DataAxesGrid.ZTitleFontFile = ''
fbm_variance_1hdf5Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5Display.DataAxesGrid.XLabelFontFile = ''
fbm_variance_1hdf5Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5Display.DataAxesGrid.YLabelFontFile = ''
fbm_variance_1hdf5Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
fbm_variance_1hdf5Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5Display.PolarAxes.PolarAxisTitleFontFile = ''
fbm_variance_1hdf5Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5Display.PolarAxes.PolarAxisLabelFontFile = ''
fbm_variance_1hdf5Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5Display.PolarAxes.LastRadialAxisTextFontFile = ''
fbm_variance_1hdf5Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(fbm_variance_1hdf5Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
fbm_variance_1hdf5Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
fbm_variance_1hdf5Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'rho'
rhoLUT = GetColorTransferFunction('rho')
rhoLUT.RGBPoints = [0.8024289608001709, 0.231373, 0.298039, 0.752941, 1.602408766746521, 0.865003, 0.865003, 0.865003, 2.402388572692871, 0.705882, 0.0156863, 0.14902]
rhoLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'rho'
rhoPWF = GetOpacityTransferFunction('rho')
rhoPWF.Points = [0.8024289608001709, 0.0, 0.5, 0.0, 2.402388572692871, 1.0, 0.5, 0.0]
rhoPWF.ScalarRangeInitialized = 1

# change representation type
fbm_variance_1hdf5Display.SetRepresentationType('Volume')

# Properties modified on rhoPWF
rhoPWF.Points = [0.8024289608001709, 0.0, 0.5, 0.0, 1.2753729820251465, 0.2720588147640228, 0.5, 0.0, 2.402388572692871, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8024289608001709, 0.0, 0.5, 0.0, 1.2753729820251465, 0.2647058963775635, 0.5, 0.0, 2.402388572692871, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8024289608001709, 0.0, 0.5, 0.0, 1.2804043292999268, 0.24264706671237946, 0.5, 0.0, 2.402388572692871, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8024289608001709, 0.0, 0.5, 0.0, 1.3005295991897583, 0.14705882966518402, 0.5, 0.0, 2.402388572692871, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8024289608001709, 0.0, 0.5, 0.0, 1.3005295991897583, 0.13970588147640228, 0.5, 0.0, 2.402388572692871, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8024289608001709, 0.0, 0.5, 0.0, 1.3055609464645386, 0.125, 0.5, 0.0, 2.402388572692871, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8024289608001709, 0.0, 0.5, 0.0, 1.3105921745300293, 0.11029411852359772, 0.5, 0.0, 2.402388572692871, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8024289608001709, 0.0, 0.5, 0.0, 1.3156235218048096, 0.07352941483259201, 0.5, 0.0, 2.402388572692871, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8024289608001709, 0.0, 0.5, 0.0, 1.3156235218048096, 0.05882352963089943, 0.5, 0.0, 2.402388572692871, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8024289608001709, 0.0, 0.5, 0.0, 1.3105921745300293, 0.029411764815449715, 0.5, 0.0, 2.402388572692871, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8024289608001709, 0.0, 0.5, 0.0, 1.3055609464645386, 0.0, 0.5, 0.0, 2.402388572692871, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8024289608001709, 0.0, 0.5, 0.0, 1.3005295991897583, 0.0, 0.5, 0.0, 2.402388572692871, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8024289608001709, 0.0, 0.5, 0.0, 2.402388572692871, 1.0, 0.5, 0.0]

# Rescale transfer function
rhoLUT.RescaleTransferFunction(1.1, 2.5)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(1.1, 2.5)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
rhoLUT.ApplyPreset('Viridis (matplotlib)', True)

# Rescale transfer function
rhoLUT.RescaleTransferFunction(1.3, 2.5)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(1.3, 2.5)

# Rescale transfer function
rhoLUT.RescaleTransferFunction(1.1, 2.5)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(1.1, 2.5)

# current camera placement for renderView1
renderView1.CameraPosition = [1089.2032867979888, 1400.3366614711492, 1213.53881179388]
renderView1.CameraFocalPoint = [255.50000000000003, 255.49999999999994, 255.50000000000006]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 442.53898133384814

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/fbb/stats/h01/fbb_variance_512_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
fbm_variance_1hdf5_1 = NetCDFReader(FileName=['/scratch/snx3000/klye/fbm/stats/H0_1/N256/fbm_variance_1.hdf5'])
fbm_variance_1hdf5_1.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(fbm_variance_1hdf5, renderView1)

# show data in view
fbm_variance_1hdf5_1Display = Show(fbm_variance_1hdf5_1, renderView1)

# trace defaults for the display properties.
fbm_variance_1hdf5_1Display.Representation = 'Outline'
fbm_variance_1hdf5_1Display.ColorArrayName = [None, '']
fbm_variance_1hdf5_1Display.OSPRayScaleArray = 'E'
fbm_variance_1hdf5_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
fbm_variance_1hdf5_1Display.SelectOrientationVectors = 'E'
fbm_variance_1hdf5_1Display.ScaleFactor = 25.5
fbm_variance_1hdf5_1Display.SelectScaleArray = 'E'
fbm_variance_1hdf5_1Display.GlyphType = 'Arrow'
fbm_variance_1hdf5_1Display.GlyphTableIndexArray = 'E'
fbm_variance_1hdf5_1Display.GaussianRadius = 1.2750000000000001
fbm_variance_1hdf5_1Display.SetScaleArray = ['POINTS', 'E']
fbm_variance_1hdf5_1Display.ScaleTransferFunction = 'PiecewiseFunction'
fbm_variance_1hdf5_1Display.OpacityArray = ['POINTS', 'E']
fbm_variance_1hdf5_1Display.OpacityTransferFunction = 'PiecewiseFunction'
fbm_variance_1hdf5_1Display.DataAxesGrid = 'GridAxesRepresentation'
fbm_variance_1hdf5_1Display.SelectionCellLabelFontFile = ''
fbm_variance_1hdf5_1Display.SelectionPointLabelFontFile = ''
fbm_variance_1hdf5_1Display.PolarAxes = 'PolarAxesRepresentation'
fbm_variance_1hdf5_1Display.ScalarOpacityUnitDistance = 1.7320508075688774
fbm_variance_1hdf5_1Display.Slice = 127

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
fbm_variance_1hdf5_1Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_1Display.DataAxesGrid.XTitleFontFile = ''
fbm_variance_1hdf5_1Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_1Display.DataAxesGrid.YTitleFontFile = ''
fbm_variance_1hdf5_1Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_1Display.DataAxesGrid.ZTitleFontFile = ''
fbm_variance_1hdf5_1Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_1Display.DataAxesGrid.XLabelFontFile = ''
fbm_variance_1hdf5_1Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_1Display.DataAxesGrid.YLabelFontFile = ''
fbm_variance_1hdf5_1Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
fbm_variance_1hdf5_1Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_1Display.PolarAxes.PolarAxisTitleFontFile = ''
fbm_variance_1hdf5_1Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_1Display.PolarAxes.PolarAxisLabelFontFile = ''
fbm_variance_1hdf5_1Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_1Display.PolarAxes.LastRadialAxisTextFontFile = ''
fbm_variance_1hdf5_1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(fbm_variance_1hdf5_1Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
fbm_variance_1hdf5_1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
fbm_variance_1hdf5_1Display.SetScalarBarVisibility(renderView1, True)

# change representation type
fbm_variance_1hdf5_1Display.SetRepresentationType('Volume')

# set active source
SetActiveSource(fbm_variance_1hdf5)

# set active source
SetActiveSource(fbm_variance_1hdf5_1)

# Rescale transfer function
rhoLUT.RescaleTransferFunction(1.1, 2.5)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(1.1, 2.5)

# current camera placement for renderView1
renderView1.CameraPosition = [543.53588675829, 698.798138307518, 605.5819902298206]
renderView1.CameraFocalPoint = [127.5, 127.5, 127.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 220.83647796503186

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/fbb/stats/h01/fbb_variance_256_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# hide data in view
Hide(fbm_variance_1hdf5_1, renderView1)

# create a new 'NetCDF Reader'
fbm_variance_1hdf5_2 = NetCDFReader(FileName=['/scratch/snx3000/klye/fbm/stats/H0_1/N128/fbm_variance_1.hdf5'])
fbm_variance_1hdf5_2.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# show data in view
fbm_variance_1hdf5_2Display = Show(fbm_variance_1hdf5_2, renderView1)

# trace defaults for the display properties.
fbm_variance_1hdf5_2Display.Representation = 'Outline'
fbm_variance_1hdf5_2Display.ColorArrayName = [None, '']
fbm_variance_1hdf5_2Display.OSPRayScaleArray = 'E'
fbm_variance_1hdf5_2Display.OSPRayScaleFunction = 'PiecewiseFunction'
fbm_variance_1hdf5_2Display.SelectOrientationVectors = 'E'
fbm_variance_1hdf5_2Display.ScaleFactor = 12.700000000000001
fbm_variance_1hdf5_2Display.SelectScaleArray = 'E'
fbm_variance_1hdf5_2Display.GlyphType = 'Arrow'
fbm_variance_1hdf5_2Display.GlyphTableIndexArray = 'E'
fbm_variance_1hdf5_2Display.GaussianRadius = 0.635
fbm_variance_1hdf5_2Display.SetScaleArray = ['POINTS', 'E']
fbm_variance_1hdf5_2Display.ScaleTransferFunction = 'PiecewiseFunction'
fbm_variance_1hdf5_2Display.OpacityArray = ['POINTS', 'E']
fbm_variance_1hdf5_2Display.OpacityTransferFunction = 'PiecewiseFunction'
fbm_variance_1hdf5_2Display.DataAxesGrid = 'GridAxesRepresentation'
fbm_variance_1hdf5_2Display.SelectionCellLabelFontFile = ''
fbm_variance_1hdf5_2Display.SelectionPointLabelFontFile = ''
fbm_variance_1hdf5_2Display.PolarAxes = 'PolarAxesRepresentation'
fbm_variance_1hdf5_2Display.ScalarOpacityUnitDistance = 1.732050807568877
fbm_variance_1hdf5_2Display.Slice = 63

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
fbm_variance_1hdf5_2Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_2Display.DataAxesGrid.XTitleFontFile = ''
fbm_variance_1hdf5_2Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_2Display.DataAxesGrid.YTitleFontFile = ''
fbm_variance_1hdf5_2Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_2Display.DataAxesGrid.ZTitleFontFile = ''
fbm_variance_1hdf5_2Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_2Display.DataAxesGrid.XLabelFontFile = ''
fbm_variance_1hdf5_2Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_2Display.DataAxesGrid.YLabelFontFile = ''
fbm_variance_1hdf5_2Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_2Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
fbm_variance_1hdf5_2Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_2Display.PolarAxes.PolarAxisTitleFontFile = ''
fbm_variance_1hdf5_2Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_2Display.PolarAxes.PolarAxisLabelFontFile = ''
fbm_variance_1hdf5_2Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_2Display.PolarAxes.LastRadialAxisTextFontFile = ''
fbm_variance_1hdf5_2Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(fbm_variance_1hdf5_2Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
fbm_variance_1hdf5_2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
fbm_variance_1hdf5_2Display.SetScalarBarVisibility(renderView1, True)

# change representation type
fbm_variance_1hdf5_2Display.SetRepresentationType('Volume')

# Rescale transfer function
rhoLUT.RescaleTransferFunction(1.1, 2.5)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(1.1, 2.5)

# current camera placement for renderView1
renderView1.CameraPosition = [270.70218673844244, 348.028876725705, 301.603579447793]
renderView1.CameraFocalPoint = [63.5, 63.5, 63.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 109.9852262806237

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/fbb/stats/h01/fbb_variance_128_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
fbm_variance_1hdf5_3 = NetCDFReader(FileName=['/scratch/snx3000/klye/fbm/stats/H0_1/N64/fbm_variance_1.hdf5'])
fbm_variance_1hdf5_3.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(fbm_variance_1hdf5_2, renderView1)

# show data in view
fbm_variance_1hdf5_3Display = Show(fbm_variance_1hdf5_3, renderView1)

# trace defaults for the display properties.
fbm_variance_1hdf5_3Display.Representation = 'Outline'
fbm_variance_1hdf5_3Display.ColorArrayName = [None, '']
fbm_variance_1hdf5_3Display.OSPRayScaleArray = 'E'
fbm_variance_1hdf5_3Display.OSPRayScaleFunction = 'PiecewiseFunction'
fbm_variance_1hdf5_3Display.SelectOrientationVectors = 'E'
fbm_variance_1hdf5_3Display.ScaleFactor = 6.300000000000001
fbm_variance_1hdf5_3Display.SelectScaleArray = 'E'
fbm_variance_1hdf5_3Display.GlyphType = 'Arrow'
fbm_variance_1hdf5_3Display.GlyphTableIndexArray = 'E'
fbm_variance_1hdf5_3Display.GaussianRadius = 0.315
fbm_variance_1hdf5_3Display.SetScaleArray = ['POINTS', 'E']
fbm_variance_1hdf5_3Display.ScaleTransferFunction = 'PiecewiseFunction'
fbm_variance_1hdf5_3Display.OpacityArray = ['POINTS', 'E']
fbm_variance_1hdf5_3Display.OpacityTransferFunction = 'PiecewiseFunction'
fbm_variance_1hdf5_3Display.DataAxesGrid = 'GridAxesRepresentation'
fbm_variance_1hdf5_3Display.SelectionCellLabelFontFile = ''
fbm_variance_1hdf5_3Display.SelectionPointLabelFontFile = ''
fbm_variance_1hdf5_3Display.PolarAxes = 'PolarAxesRepresentation'
fbm_variance_1hdf5_3Display.ScalarOpacityUnitDistance = 1.7320508075688774
fbm_variance_1hdf5_3Display.Slice = 31

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
fbm_variance_1hdf5_3Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_3Display.DataAxesGrid.XTitleFontFile = ''
fbm_variance_1hdf5_3Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_3Display.DataAxesGrid.YTitleFontFile = ''
fbm_variance_1hdf5_3Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_3Display.DataAxesGrid.ZTitleFontFile = ''
fbm_variance_1hdf5_3Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_3Display.DataAxesGrid.XLabelFontFile = ''
fbm_variance_1hdf5_3Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_3Display.DataAxesGrid.YLabelFontFile = ''
fbm_variance_1hdf5_3Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_3Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
fbm_variance_1hdf5_3Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_3Display.PolarAxes.PolarAxisTitleFontFile = ''
fbm_variance_1hdf5_3Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_3Display.PolarAxes.PolarAxisLabelFontFile = ''
fbm_variance_1hdf5_3Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_3Display.PolarAxes.LastRadialAxisTextFontFile = ''
fbm_variance_1hdf5_3Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_3Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(fbm_variance_1hdf5_3Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
fbm_variance_1hdf5_3Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
fbm_variance_1hdf5_3Display.SetScalarBarVisibility(renderView1, True)

# change representation type
fbm_variance_1hdf5_3Display.SetRepresentationType('Volume')

# Rescale transfer function
rhoLUT.RescaleTransferFunction(1.1, 2.5)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(1.1, 2.5)

# current camera placement for renderView1
renderView1.CameraPosition = [134.2853367285187, 172.64424593479856, 149.6143740567792]
renderView1.CameraFocalPoint = [31.5, 31.5, 31.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 54.559600438419636

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/fbb/stats/h01/fbb_variance_64_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# hide data in view
Hide(fbm_variance_1hdf5_3, renderView1)

# create a new 'NetCDF Reader'
fbm_mean_1hdf5 = NetCDFReader(FileName=['/scratch/snx3000/klye/fbm/stats/H0_1/N512/fbm_mean_1.hdf5'])
fbm_mean_1hdf5.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# show data in view
fbm_mean_1hdf5Display = Show(fbm_mean_1hdf5, renderView1)

# trace defaults for the display properties.
fbm_mean_1hdf5Display.Representation = 'Outline'
fbm_mean_1hdf5Display.ColorArrayName = [None, '']
fbm_mean_1hdf5Display.OSPRayScaleArray = 'E'
fbm_mean_1hdf5Display.OSPRayScaleFunction = 'PiecewiseFunction'
fbm_mean_1hdf5Display.SelectOrientationVectors = 'E'
fbm_mean_1hdf5Display.ScaleFactor = 51.1
fbm_mean_1hdf5Display.SelectScaleArray = 'E'
fbm_mean_1hdf5Display.GlyphType = 'Arrow'
fbm_mean_1hdf5Display.GlyphTableIndexArray = 'E'
fbm_mean_1hdf5Display.GaussianRadius = 2.555
fbm_mean_1hdf5Display.SetScaleArray = ['POINTS', 'E']
fbm_mean_1hdf5Display.ScaleTransferFunction = 'PiecewiseFunction'
fbm_mean_1hdf5Display.OpacityArray = ['POINTS', 'E']
fbm_mean_1hdf5Display.OpacityTransferFunction = 'PiecewiseFunction'
fbm_mean_1hdf5Display.DataAxesGrid = 'GridAxesRepresentation'
fbm_mean_1hdf5Display.SelectionCellLabelFontFile = ''
fbm_mean_1hdf5Display.SelectionPointLabelFontFile = ''
fbm_mean_1hdf5Display.PolarAxes = 'PolarAxesRepresentation'
fbm_mean_1hdf5Display.ScalarOpacityUnitDistance = 1.732050807568877
fbm_mean_1hdf5Display.Slice = 255

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
fbm_mean_1hdf5Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5Display.DataAxesGrid.XTitleFontFile = ''
fbm_mean_1hdf5Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5Display.DataAxesGrid.YTitleFontFile = ''
fbm_mean_1hdf5Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5Display.DataAxesGrid.ZTitleFontFile = ''
fbm_mean_1hdf5Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5Display.DataAxesGrid.XLabelFontFile = ''
fbm_mean_1hdf5Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5Display.DataAxesGrid.YLabelFontFile = ''
fbm_mean_1hdf5Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
fbm_mean_1hdf5Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5Display.PolarAxes.PolarAxisTitleFontFile = ''
fbm_mean_1hdf5Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5Display.PolarAxes.PolarAxisLabelFontFile = ''
fbm_mean_1hdf5Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5Display.PolarAxes.LastRadialAxisTextFontFile = ''
fbm_mean_1hdf5Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(fbm_mean_1hdf5Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
fbm_mean_1hdf5Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
fbm_mean_1hdf5Display.SetScalarBarVisibility(renderView1, True)

# change representation type
fbm_mean_1hdf5Display.SetRepresentationType('Volume')

# Rescale transfer function
rhoLUT.RescaleTransferFunction(1.1, 4.5)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(1.1, 4.5)

# Rescale transfer function
rhoLUT.RescaleTransferFunction(1.1, 5.0)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(1.1, 5.0)

# Rescale transfer function
rhoLUT.RescaleTransferFunction(2.1, 5.0)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(2.1, 5.0)

# rescale color and/or opacity maps used to exactly fit the current data range
fbm_mean_1hdf5Display.RescaleTransferFunctionToDataRange(False, True)

# current camera placement for renderView1
renderView1.CameraPosition = [1089.203286797985, 1400.3366614711435, 1213.5388117938758]
renderView1.CameraFocalPoint = [255.5, 255.5, 255.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 442.53898133384814

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/fbb/stats/h01/fbb_mean_512_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
fbm_mean_1hdf5_1 = NetCDFReader(FileName=['/scratch/snx3000/klye/fbm/stats/H0_1/N256/fbm_mean_1.hdf5'])
fbm_mean_1hdf5_1.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(fbm_mean_1hdf5, renderView1)

# show data in view
fbm_mean_1hdf5_1Display = Show(fbm_mean_1hdf5_1, renderView1)

# trace defaults for the display properties.
fbm_mean_1hdf5_1Display.Representation = 'Outline'
fbm_mean_1hdf5_1Display.ColorArrayName = [None, '']
fbm_mean_1hdf5_1Display.OSPRayScaleArray = 'E'
fbm_mean_1hdf5_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
fbm_mean_1hdf5_1Display.SelectOrientationVectors = 'E'
fbm_mean_1hdf5_1Display.ScaleFactor = 25.5
fbm_mean_1hdf5_1Display.SelectScaleArray = 'E'
fbm_mean_1hdf5_1Display.GlyphType = 'Arrow'
fbm_mean_1hdf5_1Display.GlyphTableIndexArray = 'E'
fbm_mean_1hdf5_1Display.GaussianRadius = 1.2750000000000001
fbm_mean_1hdf5_1Display.SetScaleArray = ['POINTS', 'E']
fbm_mean_1hdf5_1Display.ScaleTransferFunction = 'PiecewiseFunction'
fbm_mean_1hdf5_1Display.OpacityArray = ['POINTS', 'E']
fbm_mean_1hdf5_1Display.OpacityTransferFunction = 'PiecewiseFunction'
fbm_mean_1hdf5_1Display.DataAxesGrid = 'GridAxesRepresentation'
fbm_mean_1hdf5_1Display.SelectionCellLabelFontFile = ''
fbm_mean_1hdf5_1Display.SelectionPointLabelFontFile = ''
fbm_mean_1hdf5_1Display.PolarAxes = 'PolarAxesRepresentation'
fbm_mean_1hdf5_1Display.ScalarOpacityUnitDistance = 1.7320508075688774
fbm_mean_1hdf5_1Display.Slice = 127

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
fbm_mean_1hdf5_1Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_1Display.DataAxesGrid.XTitleFontFile = ''
fbm_mean_1hdf5_1Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_1Display.DataAxesGrid.YTitleFontFile = ''
fbm_mean_1hdf5_1Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_1Display.DataAxesGrid.ZTitleFontFile = ''
fbm_mean_1hdf5_1Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_1Display.DataAxesGrid.XLabelFontFile = ''
fbm_mean_1hdf5_1Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_1Display.DataAxesGrid.YLabelFontFile = ''
fbm_mean_1hdf5_1Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
fbm_mean_1hdf5_1Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_1Display.PolarAxes.PolarAxisTitleFontFile = ''
fbm_mean_1hdf5_1Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_1Display.PolarAxes.PolarAxisLabelFontFile = ''
fbm_mean_1hdf5_1Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_1Display.PolarAxes.LastRadialAxisTextFontFile = ''
fbm_mean_1hdf5_1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(fbm_mean_1hdf5_1Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
fbm_mean_1hdf5_1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
fbm_mean_1hdf5_1Display.SetScalarBarVisibility(renderView1, True)

# change representation type
fbm_mean_1hdf5_1Display.SetRepresentationType('Volume')

# current camera placement for renderView1
renderView1.CameraPosition = [543.53588675829, 698.7981383075178, 605.5819902298206]
renderView1.CameraFocalPoint = [127.5, 127.5, 127.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 220.83647796503186

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/fbb/stats/h01/fbb_mean_256_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
fbm_mean_1hdf5_2 = NetCDFReader(FileName=['/scratch/snx3000/klye/fbm/stats/H0_1/N128/fbm_mean_1.hdf5'])
fbm_mean_1hdf5_2.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(fbm_mean_1hdf5_1, renderView1)

# show data in view
fbm_mean_1hdf5_2Display = Show(fbm_mean_1hdf5_2, renderView1)

# trace defaults for the display properties.
fbm_mean_1hdf5_2Display.Representation = 'Outline'
fbm_mean_1hdf5_2Display.ColorArrayName = [None, '']
fbm_mean_1hdf5_2Display.OSPRayScaleArray = 'E'
fbm_mean_1hdf5_2Display.OSPRayScaleFunction = 'PiecewiseFunction'
fbm_mean_1hdf5_2Display.SelectOrientationVectors = 'E'
fbm_mean_1hdf5_2Display.ScaleFactor = 12.700000000000001
fbm_mean_1hdf5_2Display.SelectScaleArray = 'E'
fbm_mean_1hdf5_2Display.GlyphType = 'Arrow'
fbm_mean_1hdf5_2Display.GlyphTableIndexArray = 'E'
fbm_mean_1hdf5_2Display.GaussianRadius = 0.635
fbm_mean_1hdf5_2Display.SetScaleArray = ['POINTS', 'E']
fbm_mean_1hdf5_2Display.ScaleTransferFunction = 'PiecewiseFunction'
fbm_mean_1hdf5_2Display.OpacityArray = ['POINTS', 'E']
fbm_mean_1hdf5_2Display.OpacityTransferFunction = 'PiecewiseFunction'
fbm_mean_1hdf5_2Display.DataAxesGrid = 'GridAxesRepresentation'
fbm_mean_1hdf5_2Display.SelectionCellLabelFontFile = ''
fbm_mean_1hdf5_2Display.SelectionPointLabelFontFile = ''
fbm_mean_1hdf5_2Display.PolarAxes = 'PolarAxesRepresentation'
fbm_mean_1hdf5_2Display.ScalarOpacityUnitDistance = 1.732050807568877
fbm_mean_1hdf5_2Display.Slice = 63

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
fbm_mean_1hdf5_2Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_2Display.DataAxesGrid.XTitleFontFile = ''
fbm_mean_1hdf5_2Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_2Display.DataAxesGrid.YTitleFontFile = ''
fbm_mean_1hdf5_2Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_2Display.DataAxesGrid.ZTitleFontFile = ''
fbm_mean_1hdf5_2Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_2Display.DataAxesGrid.XLabelFontFile = ''
fbm_mean_1hdf5_2Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_2Display.DataAxesGrid.YLabelFontFile = ''
fbm_mean_1hdf5_2Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_2Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
fbm_mean_1hdf5_2Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_2Display.PolarAxes.PolarAxisTitleFontFile = ''
fbm_mean_1hdf5_2Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_2Display.PolarAxes.PolarAxisLabelFontFile = ''
fbm_mean_1hdf5_2Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_2Display.PolarAxes.LastRadialAxisTextFontFile = ''
fbm_mean_1hdf5_2Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(fbm_mean_1hdf5_2Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
fbm_mean_1hdf5_2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
fbm_mean_1hdf5_2Display.SetScalarBarVisibility(renderView1, True)

# change representation type
fbm_mean_1hdf5_2Display.SetRepresentationType('Volume')

# current camera placement for renderView1
renderView1.CameraPosition = [270.7021867384425, 348.02887672570495, 301.603579447793]
renderView1.CameraFocalPoint = [63.5, 63.5, 63.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 109.9852262806237

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/fbb/stats/h01/fbb_mean_128_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
fbm_mean_1hdf5_3 = NetCDFReader(FileName=['/scratch/snx3000/klye/fbm/stats/H0_1/N64/fbm_mean_1.hdf5'])
fbm_mean_1hdf5_3.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(fbm_mean_1hdf5_2, renderView1)

# show data in view
fbm_mean_1hdf5_3Display = Show(fbm_mean_1hdf5_3, renderView1)

# trace defaults for the display properties.
fbm_mean_1hdf5_3Display.Representation = 'Outline'
fbm_mean_1hdf5_3Display.ColorArrayName = [None, '']
fbm_mean_1hdf5_3Display.OSPRayScaleArray = 'E'
fbm_mean_1hdf5_3Display.OSPRayScaleFunction = 'PiecewiseFunction'
fbm_mean_1hdf5_3Display.SelectOrientationVectors = 'E'
fbm_mean_1hdf5_3Display.ScaleFactor = 6.300000000000001
fbm_mean_1hdf5_3Display.SelectScaleArray = 'E'
fbm_mean_1hdf5_3Display.GlyphType = 'Arrow'
fbm_mean_1hdf5_3Display.GlyphTableIndexArray = 'E'
fbm_mean_1hdf5_3Display.GaussianRadius = 0.315
fbm_mean_1hdf5_3Display.SetScaleArray = ['POINTS', 'E']
fbm_mean_1hdf5_3Display.ScaleTransferFunction = 'PiecewiseFunction'
fbm_mean_1hdf5_3Display.OpacityArray = ['POINTS', 'E']
fbm_mean_1hdf5_3Display.OpacityTransferFunction = 'PiecewiseFunction'
fbm_mean_1hdf5_3Display.DataAxesGrid = 'GridAxesRepresentation'
fbm_mean_1hdf5_3Display.SelectionCellLabelFontFile = ''
fbm_mean_1hdf5_3Display.SelectionPointLabelFontFile = ''
fbm_mean_1hdf5_3Display.PolarAxes = 'PolarAxesRepresentation'
fbm_mean_1hdf5_3Display.ScalarOpacityUnitDistance = 1.7320508075688774
fbm_mean_1hdf5_3Display.Slice = 31

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
fbm_mean_1hdf5_3Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_3Display.DataAxesGrid.XTitleFontFile = ''
fbm_mean_1hdf5_3Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_3Display.DataAxesGrid.YTitleFontFile = ''
fbm_mean_1hdf5_3Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_3Display.DataAxesGrid.ZTitleFontFile = ''
fbm_mean_1hdf5_3Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_3Display.DataAxesGrid.XLabelFontFile = ''
fbm_mean_1hdf5_3Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_3Display.DataAxesGrid.YLabelFontFile = ''
fbm_mean_1hdf5_3Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_3Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
fbm_mean_1hdf5_3Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_3Display.PolarAxes.PolarAxisTitleFontFile = ''
fbm_mean_1hdf5_3Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_3Display.PolarAxes.PolarAxisLabelFontFile = ''
fbm_mean_1hdf5_3Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_3Display.PolarAxes.LastRadialAxisTextFontFile = ''
fbm_mean_1hdf5_3Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_3Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(fbm_mean_1hdf5_3Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
fbm_mean_1hdf5_3Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
fbm_mean_1hdf5_3Display.SetScalarBarVisibility(renderView1, True)

# change representation type
fbm_mean_1hdf5_3Display.SetRepresentationType('Volume')

# current camera placement for renderView1
renderView1.CameraPosition = [134.28533672851873, 172.64424593479853, 149.6143740567792]
renderView1.CameraFocalPoint = [31.5, 31.5, 31.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 54.559600438419636

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/fbb/stats/h01/fbb_mean_64_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# hide data in view
Hide(fbm_mean_1hdf5_3, renderView1)

# set active source
SetActiveSource(fbm_variance_1hdf5)

# destroy fbm_variance_1hdf5
Delete(fbm_variance_1hdf5)
del fbm_variance_1hdf5

# set active source
SetActiveSource(fbm_variance_1hdf5_1)

# destroy fbm_variance_1hdf5_1
Delete(fbm_variance_1hdf5_1)
del fbm_variance_1hdf5_1

# set active source
SetActiveSource(fbm_variance_1hdf5_2)

# destroy fbm_variance_1hdf5_2
Delete(fbm_variance_1hdf5_2)
del fbm_variance_1hdf5_2

# set active source
SetActiveSource(fbm_variance_1hdf5_3)

# destroy fbm_variance_1hdf5_3
Delete(fbm_variance_1hdf5_3)
del fbm_variance_1hdf5_3

# set active source
SetActiveSource(fbm_mean_1hdf5)

# destroy fbm_mean_1hdf5
Delete(fbm_mean_1hdf5)
del fbm_mean_1hdf5

# set active source
SetActiveSource(fbm_mean_1hdf5_1)

# destroy fbm_mean_1hdf5_1
Delete(fbm_mean_1hdf5_1)
del fbm_mean_1hdf5_1

# set active source
SetActiveSource(fbm_mean_1hdf5_2)

# destroy fbm_mean_1hdf5_2
Delete(fbm_mean_1hdf5_2)
del fbm_mean_1hdf5_2

# set active source
SetActiveSource(fbm_mean_1hdf5_3)

# destroy fbm_mean_1hdf5_3
Delete(fbm_mean_1hdf5_3)
del fbm_mean_1hdf5_3

# create a new 'NetCDF Reader'
fbm_mean_1hdf5 = NetCDFReader(FileName=['/scratch/snx3000/klye/fbm/stats/H0_5/N512/fbm_mean_1.hdf5'])
fbm_mean_1hdf5.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# show data in view
fbm_mean_1hdf5Display = Show(fbm_mean_1hdf5, renderView1)

# trace defaults for the display properties.
fbm_mean_1hdf5Display.Representation = 'Outline'
fbm_mean_1hdf5Display.ColorArrayName = [None, '']
fbm_mean_1hdf5Display.OSPRayScaleArray = 'E'
fbm_mean_1hdf5Display.OSPRayScaleFunction = 'PiecewiseFunction'
fbm_mean_1hdf5Display.SelectOrientationVectors = 'E'
fbm_mean_1hdf5Display.ScaleFactor = 51.1
fbm_mean_1hdf5Display.SelectScaleArray = 'E'
fbm_mean_1hdf5Display.GlyphType = 'Arrow'
fbm_mean_1hdf5Display.GlyphTableIndexArray = 'E'
fbm_mean_1hdf5Display.GaussianRadius = 2.555
fbm_mean_1hdf5Display.SetScaleArray = ['POINTS', 'E']
fbm_mean_1hdf5Display.ScaleTransferFunction = 'PiecewiseFunction'
fbm_mean_1hdf5Display.OpacityArray = ['POINTS', 'E']
fbm_mean_1hdf5Display.OpacityTransferFunction = 'PiecewiseFunction'
fbm_mean_1hdf5Display.DataAxesGrid = 'GridAxesRepresentation'
fbm_mean_1hdf5Display.SelectionCellLabelFontFile = ''
fbm_mean_1hdf5Display.SelectionPointLabelFontFile = ''
fbm_mean_1hdf5Display.PolarAxes = 'PolarAxesRepresentation'
fbm_mean_1hdf5Display.ScalarOpacityUnitDistance = 1.732050807568877
fbm_mean_1hdf5Display.Slice = 255

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
fbm_mean_1hdf5Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5Display.DataAxesGrid.XTitleFontFile = ''
fbm_mean_1hdf5Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5Display.DataAxesGrid.YTitleFontFile = ''
fbm_mean_1hdf5Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5Display.DataAxesGrid.ZTitleFontFile = ''
fbm_mean_1hdf5Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5Display.DataAxesGrid.XLabelFontFile = ''
fbm_mean_1hdf5Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5Display.DataAxesGrid.YLabelFontFile = ''
fbm_mean_1hdf5Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
fbm_mean_1hdf5Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5Display.PolarAxes.PolarAxisTitleFontFile = ''
fbm_mean_1hdf5Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5Display.PolarAxes.PolarAxisLabelFontFile = ''
fbm_mean_1hdf5Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5Display.PolarAxes.LastRadialAxisTextFontFile = ''
fbm_mean_1hdf5Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(fbm_mean_1hdf5Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
fbm_mean_1hdf5Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
fbm_mean_1hdf5Display.SetScalarBarVisibility(renderView1, True)

# change representation type
fbm_mean_1hdf5Display.SetRepresentationType('Volume')

# rescale color and/or opacity maps used to exactly fit the current data range
fbm_mean_1hdf5Display.RescaleTransferFunctionToDataRange(False, True)

# Rescale transfer function
rhoLUT.RescaleTransferFunction(3.5, 4.4)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(3.5, 4.4)

# current camera placement for renderView1
renderView1.CameraPosition = [1089.2032867979851, 1400.3366614711435, 1213.5388117938758]
renderView1.CameraFocalPoint = [255.5, 255.5, 255.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 442.53898133384814

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/fbb/stats/h05/fbb_mean_512_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
fbm_mean_1hdf5_1 = NetCDFReader(FileName=['/scratch/snx3000/klye/fbm/stats/H0_5/N256/fbm_mean_1.hdf5'])
fbm_mean_1hdf5_1.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(fbm_mean_1hdf5, renderView1)

# show data in view
fbm_mean_1hdf5_1Display = Show(fbm_mean_1hdf5_1, renderView1)

# trace defaults for the display properties.
fbm_mean_1hdf5_1Display.Representation = 'Outline'
fbm_mean_1hdf5_1Display.ColorArrayName = [None, '']
fbm_mean_1hdf5_1Display.OSPRayScaleArray = 'E'
fbm_mean_1hdf5_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
fbm_mean_1hdf5_1Display.SelectOrientationVectors = 'E'
fbm_mean_1hdf5_1Display.ScaleFactor = 25.5
fbm_mean_1hdf5_1Display.SelectScaleArray = 'E'
fbm_mean_1hdf5_1Display.GlyphType = 'Arrow'
fbm_mean_1hdf5_1Display.GlyphTableIndexArray = 'E'
fbm_mean_1hdf5_1Display.GaussianRadius = 1.2750000000000001
fbm_mean_1hdf5_1Display.SetScaleArray = ['POINTS', 'E']
fbm_mean_1hdf5_1Display.ScaleTransferFunction = 'PiecewiseFunction'
fbm_mean_1hdf5_1Display.OpacityArray = ['POINTS', 'E']
fbm_mean_1hdf5_1Display.OpacityTransferFunction = 'PiecewiseFunction'
fbm_mean_1hdf5_1Display.DataAxesGrid = 'GridAxesRepresentation'
fbm_mean_1hdf5_1Display.SelectionCellLabelFontFile = ''
fbm_mean_1hdf5_1Display.SelectionPointLabelFontFile = ''
fbm_mean_1hdf5_1Display.PolarAxes = 'PolarAxesRepresentation'
fbm_mean_1hdf5_1Display.ScalarOpacityUnitDistance = 1.7320508075688774
fbm_mean_1hdf5_1Display.Slice = 127

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
fbm_mean_1hdf5_1Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_1Display.DataAxesGrid.XTitleFontFile = ''
fbm_mean_1hdf5_1Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_1Display.DataAxesGrid.YTitleFontFile = ''
fbm_mean_1hdf5_1Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_1Display.DataAxesGrid.ZTitleFontFile = ''
fbm_mean_1hdf5_1Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_1Display.DataAxesGrid.XLabelFontFile = ''
fbm_mean_1hdf5_1Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_1Display.DataAxesGrid.YLabelFontFile = ''
fbm_mean_1hdf5_1Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
fbm_mean_1hdf5_1Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_1Display.PolarAxes.PolarAxisTitleFontFile = ''
fbm_mean_1hdf5_1Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_1Display.PolarAxes.PolarAxisLabelFontFile = ''
fbm_mean_1hdf5_1Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_1Display.PolarAxes.LastRadialAxisTextFontFile = ''
fbm_mean_1hdf5_1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(fbm_mean_1hdf5_1Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
fbm_mean_1hdf5_1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
fbm_mean_1hdf5_1Display.SetScalarBarVisibility(renderView1, True)

# change representation type
fbm_mean_1hdf5_1Display.SetRepresentationType('Volume')

# current camera placement for renderView1
renderView1.CameraPosition = [543.5358867582901, 698.7981383075178, 605.5819902298206]
renderView1.CameraFocalPoint = [127.5, 127.5, 127.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 220.83647796503186

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/fbb/stats/h05/fbb_mean_256_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
fbm_mean_1hdf5_2 = NetCDFReader(FileName=['/scratch/snx3000/klye/fbm/stats/H0_5/N128/fbm_mean_1.hdf5'])
fbm_mean_1hdf5_2.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(fbm_mean_1hdf5_1, renderView1)

# show data in view
fbm_mean_1hdf5_2Display = Show(fbm_mean_1hdf5_2, renderView1)

# trace defaults for the display properties.
fbm_mean_1hdf5_2Display.Representation = 'Outline'
fbm_mean_1hdf5_2Display.ColorArrayName = [None, '']
fbm_mean_1hdf5_2Display.OSPRayScaleArray = 'E'
fbm_mean_1hdf5_2Display.OSPRayScaleFunction = 'PiecewiseFunction'
fbm_mean_1hdf5_2Display.SelectOrientationVectors = 'E'
fbm_mean_1hdf5_2Display.ScaleFactor = 12.700000000000001
fbm_mean_1hdf5_2Display.SelectScaleArray = 'E'
fbm_mean_1hdf5_2Display.GlyphType = 'Arrow'
fbm_mean_1hdf5_2Display.GlyphTableIndexArray = 'E'
fbm_mean_1hdf5_2Display.GaussianRadius = 0.635
fbm_mean_1hdf5_2Display.SetScaleArray = ['POINTS', 'E']
fbm_mean_1hdf5_2Display.ScaleTransferFunction = 'PiecewiseFunction'
fbm_mean_1hdf5_2Display.OpacityArray = ['POINTS', 'E']
fbm_mean_1hdf5_2Display.OpacityTransferFunction = 'PiecewiseFunction'
fbm_mean_1hdf5_2Display.DataAxesGrid = 'GridAxesRepresentation'
fbm_mean_1hdf5_2Display.SelectionCellLabelFontFile = ''
fbm_mean_1hdf5_2Display.SelectionPointLabelFontFile = ''
fbm_mean_1hdf5_2Display.PolarAxes = 'PolarAxesRepresentation'
fbm_mean_1hdf5_2Display.ScalarOpacityUnitDistance = 1.732050807568877
fbm_mean_1hdf5_2Display.Slice = 63

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
fbm_mean_1hdf5_2Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_2Display.DataAxesGrid.XTitleFontFile = ''
fbm_mean_1hdf5_2Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_2Display.DataAxesGrid.YTitleFontFile = ''
fbm_mean_1hdf5_2Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_2Display.DataAxesGrid.ZTitleFontFile = ''
fbm_mean_1hdf5_2Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_2Display.DataAxesGrid.XLabelFontFile = ''
fbm_mean_1hdf5_2Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_2Display.DataAxesGrid.YLabelFontFile = ''
fbm_mean_1hdf5_2Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_2Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
fbm_mean_1hdf5_2Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_2Display.PolarAxes.PolarAxisTitleFontFile = ''
fbm_mean_1hdf5_2Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_2Display.PolarAxes.PolarAxisLabelFontFile = ''
fbm_mean_1hdf5_2Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_2Display.PolarAxes.LastRadialAxisTextFontFile = ''
fbm_mean_1hdf5_2Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(fbm_mean_1hdf5_2Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
fbm_mean_1hdf5_2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
fbm_mean_1hdf5_2Display.SetScalarBarVisibility(renderView1, True)

# change representation type
fbm_mean_1hdf5_2Display.SetRepresentationType('Volume')

# current camera placement for renderView1
renderView1.CameraPosition = [270.7021867384425, 348.0288767257049, 301.603579447793]
renderView1.CameraFocalPoint = [63.5, 63.5, 63.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 109.9852262806237

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/fbb/stats/h05/fbb_mean_128_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
fbm_mean_1hdf5_3 = NetCDFReader(FileName=['/scratch/snx3000/klye/fbm/stats/H0_5/N64/fbm_mean_1.hdf5'])
fbm_mean_1hdf5_3.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(fbm_mean_1hdf5_2, renderView1)

# show data in view
fbm_mean_1hdf5_3Display = Show(fbm_mean_1hdf5_3, renderView1)

# trace defaults for the display properties.
fbm_mean_1hdf5_3Display.Representation = 'Outline'
fbm_mean_1hdf5_3Display.ColorArrayName = [None, '']
fbm_mean_1hdf5_3Display.OSPRayScaleArray = 'E'
fbm_mean_1hdf5_3Display.OSPRayScaleFunction = 'PiecewiseFunction'
fbm_mean_1hdf5_3Display.SelectOrientationVectors = 'E'
fbm_mean_1hdf5_3Display.ScaleFactor = 6.300000000000001
fbm_mean_1hdf5_3Display.SelectScaleArray = 'E'
fbm_mean_1hdf5_3Display.GlyphType = 'Arrow'
fbm_mean_1hdf5_3Display.GlyphTableIndexArray = 'E'
fbm_mean_1hdf5_3Display.GaussianRadius = 0.315
fbm_mean_1hdf5_3Display.SetScaleArray = ['POINTS', 'E']
fbm_mean_1hdf5_3Display.ScaleTransferFunction = 'PiecewiseFunction'
fbm_mean_1hdf5_3Display.OpacityArray = ['POINTS', 'E']
fbm_mean_1hdf5_3Display.OpacityTransferFunction = 'PiecewiseFunction'
fbm_mean_1hdf5_3Display.DataAxesGrid = 'GridAxesRepresentation'
fbm_mean_1hdf5_3Display.SelectionCellLabelFontFile = ''
fbm_mean_1hdf5_3Display.SelectionPointLabelFontFile = ''
fbm_mean_1hdf5_3Display.PolarAxes = 'PolarAxesRepresentation'
fbm_mean_1hdf5_3Display.ScalarOpacityUnitDistance = 1.7320508075688774
fbm_mean_1hdf5_3Display.Slice = 31

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
fbm_mean_1hdf5_3Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_3Display.DataAxesGrid.XTitleFontFile = ''
fbm_mean_1hdf5_3Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_3Display.DataAxesGrid.YTitleFontFile = ''
fbm_mean_1hdf5_3Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_3Display.DataAxesGrid.ZTitleFontFile = ''
fbm_mean_1hdf5_3Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_3Display.DataAxesGrid.XLabelFontFile = ''
fbm_mean_1hdf5_3Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_3Display.DataAxesGrid.YLabelFontFile = ''
fbm_mean_1hdf5_3Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_3Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
fbm_mean_1hdf5_3Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_3Display.PolarAxes.PolarAxisTitleFontFile = ''
fbm_mean_1hdf5_3Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_3Display.PolarAxes.PolarAxisLabelFontFile = ''
fbm_mean_1hdf5_3Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_3Display.PolarAxes.LastRadialAxisTextFontFile = ''
fbm_mean_1hdf5_3Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_3Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(fbm_mean_1hdf5_3Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
fbm_mean_1hdf5_3Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
fbm_mean_1hdf5_3Display.SetScalarBarVisibility(renderView1, True)

# change representation type
fbm_mean_1hdf5_3Display.SetRepresentationType('Volume')

# current camera placement for renderView1
renderView1.CameraPosition = [134.28533672851876, 172.64424593479853, 149.6143740567792]
renderView1.CameraFocalPoint = [31.5, 31.5, 31.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 54.559600438419636

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/fbb/stats/h05/fbb_mean_64_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# hide data in view
Hide(fbm_mean_1hdf5_3, renderView1)

# create a new 'NetCDF Reader'
fbm_variance_1hdf5 = NetCDFReader(FileName=['/scratch/snx3000/klye/fbm/stats/H0_5/N512/fbm_variance_1.hdf5'])
fbm_variance_1hdf5.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# show data in view
fbm_variance_1hdf5Display = Show(fbm_variance_1hdf5, renderView1)

# trace defaults for the display properties.
fbm_variance_1hdf5Display.Representation = 'Outline'
fbm_variance_1hdf5Display.ColorArrayName = [None, '']
fbm_variance_1hdf5Display.OSPRayScaleArray = 'E'
fbm_variance_1hdf5Display.OSPRayScaleFunction = 'PiecewiseFunction'
fbm_variance_1hdf5Display.SelectOrientationVectors = 'E'
fbm_variance_1hdf5Display.ScaleFactor = 51.1
fbm_variance_1hdf5Display.SelectScaleArray = 'E'
fbm_variance_1hdf5Display.GlyphType = 'Arrow'
fbm_variance_1hdf5Display.GlyphTableIndexArray = 'E'
fbm_variance_1hdf5Display.GaussianRadius = 2.555
fbm_variance_1hdf5Display.SetScaleArray = ['POINTS', 'E']
fbm_variance_1hdf5Display.ScaleTransferFunction = 'PiecewiseFunction'
fbm_variance_1hdf5Display.OpacityArray = ['POINTS', 'E']
fbm_variance_1hdf5Display.OpacityTransferFunction = 'PiecewiseFunction'
fbm_variance_1hdf5Display.DataAxesGrid = 'GridAxesRepresentation'
fbm_variance_1hdf5Display.SelectionCellLabelFontFile = ''
fbm_variance_1hdf5Display.SelectionPointLabelFontFile = ''
fbm_variance_1hdf5Display.PolarAxes = 'PolarAxesRepresentation'
fbm_variance_1hdf5Display.ScalarOpacityUnitDistance = 1.732050807568877
fbm_variance_1hdf5Display.Slice = 255

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
fbm_variance_1hdf5Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5Display.DataAxesGrid.XTitleFontFile = ''
fbm_variance_1hdf5Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5Display.DataAxesGrid.YTitleFontFile = ''
fbm_variance_1hdf5Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5Display.DataAxesGrid.ZTitleFontFile = ''
fbm_variance_1hdf5Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5Display.DataAxesGrid.XLabelFontFile = ''
fbm_variance_1hdf5Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5Display.DataAxesGrid.YLabelFontFile = ''
fbm_variance_1hdf5Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
fbm_variance_1hdf5Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5Display.PolarAxes.PolarAxisTitleFontFile = ''
fbm_variance_1hdf5Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5Display.PolarAxes.PolarAxisLabelFontFile = ''
fbm_variance_1hdf5Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5Display.PolarAxes.LastRadialAxisTextFontFile = ''
fbm_variance_1hdf5Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(fbm_variance_1hdf5Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
fbm_variance_1hdf5Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
fbm_variance_1hdf5Display.SetScalarBarVisibility(renderView1, True)

# change representation type
fbm_variance_1hdf5Display.SetRepresentationType('Volume')

# rescale color and/or opacity maps used to exactly fit the current data range
fbm_variance_1hdf5Display.RescaleTransferFunctionToDataRange(False, True)

# Rescale transfer function
rhoLUT.RescaleTransferFunction(0.2, 0.957299292088)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(0.2, 0.957299292088)

# Rescale transfer function
rhoLUT.RescaleTransferFunction(0.2, 0.9)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(0.2, 0.9)

# Rescale transfer function
rhoLUT.RescaleTransferFunction(0.2, 0.8)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(0.2, 0.8)

# Rescale transfer function
rhoLUT.RescaleTransferFunction(0.2, 0.7)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(0.2, 0.7)

# Rescale transfer function
rhoLUT.RescaleTransferFunction(0.2, 0.6)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(0.2, 0.6)

# current camera placement for renderView1
renderView1.CameraPosition = [1089.2032867979854, 1400.3366614711435, 1213.5388117938758]
renderView1.CameraFocalPoint = [255.5, 255.5, 255.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 442.53898133384814

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/fbb/stats/h05/fbb_variance_512_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
fbm_variance_1hdf5_1 = NetCDFReader(FileName=['/scratch/snx3000/klye/fbm/stats/H0_5/N256/fbm_variance_1.hdf5'])
fbm_variance_1hdf5_1.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(fbm_variance_1hdf5, renderView1)

# show data in view
fbm_variance_1hdf5_1Display = Show(fbm_variance_1hdf5_1, renderView1)

# trace defaults for the display properties.
fbm_variance_1hdf5_1Display.Representation = 'Outline'
fbm_variance_1hdf5_1Display.ColorArrayName = [None, '']
fbm_variance_1hdf5_1Display.OSPRayScaleArray = 'E'
fbm_variance_1hdf5_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
fbm_variance_1hdf5_1Display.SelectOrientationVectors = 'E'
fbm_variance_1hdf5_1Display.ScaleFactor = 25.5
fbm_variance_1hdf5_1Display.SelectScaleArray = 'E'
fbm_variance_1hdf5_1Display.GlyphType = 'Arrow'
fbm_variance_1hdf5_1Display.GlyphTableIndexArray = 'E'
fbm_variance_1hdf5_1Display.GaussianRadius = 1.2750000000000001
fbm_variance_1hdf5_1Display.SetScaleArray = ['POINTS', 'E']
fbm_variance_1hdf5_1Display.ScaleTransferFunction = 'PiecewiseFunction'
fbm_variance_1hdf5_1Display.OpacityArray = ['POINTS', 'E']
fbm_variance_1hdf5_1Display.OpacityTransferFunction = 'PiecewiseFunction'
fbm_variance_1hdf5_1Display.DataAxesGrid = 'GridAxesRepresentation'
fbm_variance_1hdf5_1Display.SelectionCellLabelFontFile = ''
fbm_variance_1hdf5_1Display.SelectionPointLabelFontFile = ''
fbm_variance_1hdf5_1Display.PolarAxes = 'PolarAxesRepresentation'
fbm_variance_1hdf5_1Display.ScalarOpacityUnitDistance = 1.7320508075688774
fbm_variance_1hdf5_1Display.Slice = 127

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
fbm_variance_1hdf5_1Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_1Display.DataAxesGrid.XTitleFontFile = ''
fbm_variance_1hdf5_1Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_1Display.DataAxesGrid.YTitleFontFile = ''
fbm_variance_1hdf5_1Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_1Display.DataAxesGrid.ZTitleFontFile = ''
fbm_variance_1hdf5_1Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_1Display.DataAxesGrid.XLabelFontFile = ''
fbm_variance_1hdf5_1Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_1Display.DataAxesGrid.YLabelFontFile = ''
fbm_variance_1hdf5_1Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
fbm_variance_1hdf5_1Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_1Display.PolarAxes.PolarAxisTitleFontFile = ''
fbm_variance_1hdf5_1Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_1Display.PolarAxes.PolarAxisLabelFontFile = ''
fbm_variance_1hdf5_1Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_1Display.PolarAxes.LastRadialAxisTextFontFile = ''
fbm_variance_1hdf5_1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(fbm_variance_1hdf5_1Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
fbm_variance_1hdf5_1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
fbm_variance_1hdf5_1Display.SetScalarBarVisibility(renderView1, True)

# change representation type
fbm_variance_1hdf5_1Display.SetRepresentationType('Volume')

# Rescale transfer function
rhoLUT.RescaleTransferFunction(0.2, 0.8)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(0.2, 0.8)

# Rescale transfer function
rhoLUT.RescaleTransferFunction(0.2, 0.7)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(0.2, 0.7)

# hide data in view
Hide(fbm_variance_1hdf5_1, renderView1)

# set active source
SetActiveSource(fbm_variance_1hdf5)

# show data in view
fbm_variance_1hdf5Display = Show(fbm_variance_1hdf5, renderView1)

# show color bar/color legend
fbm_variance_1hdf5Display.SetScalarBarVisibility(renderView1, True)

# reset view to fit data
renderView1.ResetCamera()

# Rescale transfer function
rhoLUT.RescaleTransferFunction(0.2, 0.6)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(0.2, 0.6)

# hide data in view
Hide(fbm_variance_1hdf5, renderView1)

# set active source
SetActiveSource(fbm_variance_1hdf5_1)

# show data in view
fbm_variance_1hdf5_1Display = Show(fbm_variance_1hdf5_1, renderView1)

# show color bar/color legend
fbm_variance_1hdf5_1Display.SetScalarBarVisibility(renderView1, True)

# reset view to fit data
renderView1.ResetCamera()

# current camera placement for renderView1
renderView1.CameraPosition = [543.5358867582902, 698.7981383075178, 605.5819902298206]
renderView1.CameraFocalPoint = [127.5, 127.5, 127.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 220.83647796503186

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/fbb/stats/h05/fbb_variance_256_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# hide data in view
Hide(fbm_variance_1hdf5_1, renderView1)

# create a new 'NetCDF Reader'
fbm_variance_1hdf5_2 = NetCDFReader(FileName=['/scratch/snx3000/klye/fbm/stats/H0_5/N128/fbm_variance_1.hdf5'])
fbm_variance_1hdf5_2.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# show data in view
fbm_variance_1hdf5_2Display = Show(fbm_variance_1hdf5_2, renderView1)

# trace defaults for the display properties.
fbm_variance_1hdf5_2Display.Representation = 'Outline'
fbm_variance_1hdf5_2Display.ColorArrayName = [None, '']
fbm_variance_1hdf5_2Display.OSPRayScaleArray = 'E'
fbm_variance_1hdf5_2Display.OSPRayScaleFunction = 'PiecewiseFunction'
fbm_variance_1hdf5_2Display.SelectOrientationVectors = 'E'
fbm_variance_1hdf5_2Display.ScaleFactor = 12.700000000000001
fbm_variance_1hdf5_2Display.SelectScaleArray = 'E'
fbm_variance_1hdf5_2Display.GlyphType = 'Arrow'
fbm_variance_1hdf5_2Display.GlyphTableIndexArray = 'E'
fbm_variance_1hdf5_2Display.GaussianRadius = 0.635
fbm_variance_1hdf5_2Display.SetScaleArray = ['POINTS', 'E']
fbm_variance_1hdf5_2Display.ScaleTransferFunction = 'PiecewiseFunction'
fbm_variance_1hdf5_2Display.OpacityArray = ['POINTS', 'E']
fbm_variance_1hdf5_2Display.OpacityTransferFunction = 'PiecewiseFunction'
fbm_variance_1hdf5_2Display.DataAxesGrid = 'GridAxesRepresentation'
fbm_variance_1hdf5_2Display.SelectionCellLabelFontFile = ''
fbm_variance_1hdf5_2Display.SelectionPointLabelFontFile = ''
fbm_variance_1hdf5_2Display.PolarAxes = 'PolarAxesRepresentation'
fbm_variance_1hdf5_2Display.ScalarOpacityUnitDistance = 1.732050807568877
fbm_variance_1hdf5_2Display.Slice = 63

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
fbm_variance_1hdf5_2Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_2Display.DataAxesGrid.XTitleFontFile = ''
fbm_variance_1hdf5_2Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_2Display.DataAxesGrid.YTitleFontFile = ''
fbm_variance_1hdf5_2Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_2Display.DataAxesGrid.ZTitleFontFile = ''
fbm_variance_1hdf5_2Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_2Display.DataAxesGrid.XLabelFontFile = ''
fbm_variance_1hdf5_2Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_2Display.DataAxesGrid.YLabelFontFile = ''
fbm_variance_1hdf5_2Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_2Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
fbm_variance_1hdf5_2Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_2Display.PolarAxes.PolarAxisTitleFontFile = ''
fbm_variance_1hdf5_2Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_2Display.PolarAxes.PolarAxisLabelFontFile = ''
fbm_variance_1hdf5_2Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_2Display.PolarAxes.LastRadialAxisTextFontFile = ''
fbm_variance_1hdf5_2Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(fbm_variance_1hdf5_2Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
fbm_variance_1hdf5_2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
fbm_variance_1hdf5_2Display.SetScalarBarVisibility(renderView1, True)

# change representation type
fbm_variance_1hdf5_2Display.SetRepresentationType('Volume')

# Rescale transfer function
rhoLUT.RescaleTransferFunction(0.2, 0.6)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(0.2, 0.6)

# current camera placement for renderView1
renderView1.CameraPosition = [270.70218673844255, 348.0288767257049, 301.603579447793]
renderView1.CameraFocalPoint = [63.5, 63.5, 63.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 109.9852262806237

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/fbb/stats/h05/fbb_variance_128_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
fbm_variance_1hdf5_3 = NetCDFReader(FileName=['/scratch/snx3000/klye/fbm/stats/H0_5/N64/fbm_variance_1.hdf5'])
fbm_variance_1hdf5_3.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(fbm_variance_1hdf5_2, renderView1)

# show data in view
fbm_variance_1hdf5_3Display = Show(fbm_variance_1hdf5_3, renderView1)

# trace defaults for the display properties.
fbm_variance_1hdf5_3Display.Representation = 'Outline'
fbm_variance_1hdf5_3Display.ColorArrayName = [None, '']
fbm_variance_1hdf5_3Display.OSPRayScaleArray = 'E'
fbm_variance_1hdf5_3Display.OSPRayScaleFunction = 'PiecewiseFunction'
fbm_variance_1hdf5_3Display.SelectOrientationVectors = 'E'
fbm_variance_1hdf5_3Display.ScaleFactor = 6.300000000000001
fbm_variance_1hdf5_3Display.SelectScaleArray = 'E'
fbm_variance_1hdf5_3Display.GlyphType = 'Arrow'
fbm_variance_1hdf5_3Display.GlyphTableIndexArray = 'E'
fbm_variance_1hdf5_3Display.GaussianRadius = 0.315
fbm_variance_1hdf5_3Display.SetScaleArray = ['POINTS', 'E']
fbm_variance_1hdf5_3Display.ScaleTransferFunction = 'PiecewiseFunction'
fbm_variance_1hdf5_3Display.OpacityArray = ['POINTS', 'E']
fbm_variance_1hdf5_3Display.OpacityTransferFunction = 'PiecewiseFunction'
fbm_variance_1hdf5_3Display.DataAxesGrid = 'GridAxesRepresentation'
fbm_variance_1hdf5_3Display.SelectionCellLabelFontFile = ''
fbm_variance_1hdf5_3Display.SelectionPointLabelFontFile = ''
fbm_variance_1hdf5_3Display.PolarAxes = 'PolarAxesRepresentation'
fbm_variance_1hdf5_3Display.ScalarOpacityUnitDistance = 1.7320508075688774
fbm_variance_1hdf5_3Display.Slice = 31

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
fbm_variance_1hdf5_3Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_3Display.DataAxesGrid.XTitleFontFile = ''
fbm_variance_1hdf5_3Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_3Display.DataAxesGrid.YTitleFontFile = ''
fbm_variance_1hdf5_3Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_3Display.DataAxesGrid.ZTitleFontFile = ''
fbm_variance_1hdf5_3Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_3Display.DataAxesGrid.XLabelFontFile = ''
fbm_variance_1hdf5_3Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_3Display.DataAxesGrid.YLabelFontFile = ''
fbm_variance_1hdf5_3Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_3Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
fbm_variance_1hdf5_3Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_3Display.PolarAxes.PolarAxisTitleFontFile = ''
fbm_variance_1hdf5_3Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_3Display.PolarAxes.PolarAxisLabelFontFile = ''
fbm_variance_1hdf5_3Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_3Display.PolarAxes.LastRadialAxisTextFontFile = ''
fbm_variance_1hdf5_3Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_3Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(fbm_variance_1hdf5_3Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
fbm_variance_1hdf5_3Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
fbm_variance_1hdf5_3Display.SetScalarBarVisibility(renderView1, True)

# change representation type
fbm_variance_1hdf5_3Display.SetRepresentationType('Volume')

# Rescale transfer function
rhoLUT.RescaleTransferFunction(0.2, 0.6)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(0.2, 0.6)

# current camera placement for renderView1
renderView1.CameraPosition = [134.28533672851876, 172.6442459347985, 149.6143740567792]
renderView1.CameraFocalPoint = [31.5, 31.5, 31.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 54.559600438419636

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/fbb/stats/h05/fbb_variance_64_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# hide data in view
Hide(fbm_variance_1hdf5_3, renderView1)

# create a new 'NetCDF Reader'
fbm_mean_1hdf5_4 = NetCDFReader(FileName=['/scratch/snx3000/klye/fbm/stats/H0_75/N512/fbm_mean_1.hdf5'])
fbm_mean_1hdf5_4.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# set active source
SetActiveSource(fbm_mean_1hdf5)

# destroy fbm_mean_1hdf5
Delete(fbm_mean_1hdf5)
del fbm_mean_1hdf5

# set active source
SetActiveSource(fbm_mean_1hdf5_1)

# destroy fbm_mean_1hdf5_1
Delete(fbm_mean_1hdf5_1)
del fbm_mean_1hdf5_1

# set active source
SetActiveSource(fbm_mean_1hdf5_2)

# destroy fbm_mean_1hdf5_2
Delete(fbm_mean_1hdf5_2)
del fbm_mean_1hdf5_2

# set active source
SetActiveSource(fbm_mean_1hdf5_3)

# destroy fbm_mean_1hdf5_3
Delete(fbm_mean_1hdf5_3)
del fbm_mean_1hdf5_3

# set active source
SetActiveSource(fbm_variance_1hdf5)

# destroy fbm_variance_1hdf5
Delete(fbm_variance_1hdf5)
del fbm_variance_1hdf5

# set active source
SetActiveSource(fbm_variance_1hdf5_1)

# destroy fbm_variance_1hdf5_1
Delete(fbm_variance_1hdf5_1)
del fbm_variance_1hdf5_1

# set active source
SetActiveSource(fbm_variance_1hdf5_2)

# destroy fbm_variance_1hdf5_2
Delete(fbm_variance_1hdf5_2)
del fbm_variance_1hdf5_2

# set active source
SetActiveSource(fbm_variance_1hdf5_3)

# destroy fbm_variance_1hdf5_3
Delete(fbm_variance_1hdf5_3)
del fbm_variance_1hdf5_3

# set active source
SetActiveSource(fbm_mean_1hdf5_4)

# show data in view
fbm_mean_1hdf5_4Display = Show(fbm_mean_1hdf5_4, renderView1)

# trace defaults for the display properties.
fbm_mean_1hdf5_4Display.Representation = 'Outline'
fbm_mean_1hdf5_4Display.ColorArrayName = [None, '']
fbm_mean_1hdf5_4Display.OSPRayScaleArray = 'E'
fbm_mean_1hdf5_4Display.OSPRayScaleFunction = 'PiecewiseFunction'
fbm_mean_1hdf5_4Display.SelectOrientationVectors = 'E'
fbm_mean_1hdf5_4Display.ScaleFactor = 51.1
fbm_mean_1hdf5_4Display.SelectScaleArray = 'E'
fbm_mean_1hdf5_4Display.GlyphType = 'Arrow'
fbm_mean_1hdf5_4Display.GlyphTableIndexArray = 'E'
fbm_mean_1hdf5_4Display.GaussianRadius = 2.555
fbm_mean_1hdf5_4Display.SetScaleArray = ['POINTS', 'E']
fbm_mean_1hdf5_4Display.ScaleTransferFunction = 'PiecewiseFunction'
fbm_mean_1hdf5_4Display.OpacityArray = ['POINTS', 'E']
fbm_mean_1hdf5_4Display.OpacityTransferFunction = 'PiecewiseFunction'
fbm_mean_1hdf5_4Display.DataAxesGrid = 'GridAxesRepresentation'
fbm_mean_1hdf5_4Display.SelectionCellLabelFontFile = ''
fbm_mean_1hdf5_4Display.SelectionPointLabelFontFile = ''
fbm_mean_1hdf5_4Display.PolarAxes = 'PolarAxesRepresentation'
fbm_mean_1hdf5_4Display.ScalarOpacityUnitDistance = 1.732050807568877
fbm_mean_1hdf5_4Display.Slice = 255

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
fbm_mean_1hdf5_4Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_4Display.DataAxesGrid.XTitleFontFile = ''
fbm_mean_1hdf5_4Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_4Display.DataAxesGrid.YTitleFontFile = ''
fbm_mean_1hdf5_4Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_4Display.DataAxesGrid.ZTitleFontFile = ''
fbm_mean_1hdf5_4Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_4Display.DataAxesGrid.XLabelFontFile = ''
fbm_mean_1hdf5_4Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_4Display.DataAxesGrid.YLabelFontFile = ''
fbm_mean_1hdf5_4Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_4Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
fbm_mean_1hdf5_4Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_4Display.PolarAxes.PolarAxisTitleFontFile = ''
fbm_mean_1hdf5_4Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_4Display.PolarAxes.PolarAxisLabelFontFile = ''
fbm_mean_1hdf5_4Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_4Display.PolarAxes.LastRadialAxisTextFontFile = ''
fbm_mean_1hdf5_4Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_4Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(fbm_mean_1hdf5_4Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
fbm_mean_1hdf5_4Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
fbm_mean_1hdf5_4Display.SetScalarBarVisibility(renderView1, True)

# change representation type
fbm_mean_1hdf5_4Display.SetRepresentationType('Volume')

# rescale color and/or opacity maps used to exactly fit the current data range
fbm_mean_1hdf5_4Display.RescaleTransferFunctionToDataRange(False, True)

# Rescale transfer function
rhoLUT.RescaleTransferFunction(3.7, 4.2)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(3.7, 4.2)

# Rescale transfer function
rhoLUT.RescaleTransferFunction(3.7, 4.15)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(3.7, 4.15)

# current camera placement for renderView1
renderView1.CameraPosition = [1089.2032867979856, 1400.3366614711435, 1213.538811793876]
renderView1.CameraFocalPoint = [255.5, 255.5, 255.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 442.53898133384814

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/fbb/stats/h075/fbb_mean_512_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
fbm_variance_1hdf5 = NetCDFReader(FileName=['/scratch/snx3000/klye/fbm/stats/H0_75/N256/fbm_variance_1.hdf5'])
fbm_variance_1hdf5.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# destroy fbm_variance_1hdf5
Delete(fbm_variance_1hdf5)
del fbm_variance_1hdf5

# create a new 'NetCDF Reader'
fbm_mean_1hdf5 = NetCDFReader(FileName=['/scratch/snx3000/klye/fbm/stats/H0_75/N256/fbm_mean_1.hdf5'])
fbm_mean_1hdf5.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(fbm_mean_1hdf5_4, renderView1)

# show data in view
fbm_mean_1hdf5Display = Show(fbm_mean_1hdf5, renderView1)

# trace defaults for the display properties.
fbm_mean_1hdf5Display.Representation = 'Outline'
fbm_mean_1hdf5Display.ColorArrayName = [None, '']
fbm_mean_1hdf5Display.OSPRayScaleArray = 'E'
fbm_mean_1hdf5Display.OSPRayScaleFunction = 'PiecewiseFunction'
fbm_mean_1hdf5Display.SelectOrientationVectors = 'E'
fbm_mean_1hdf5Display.ScaleFactor = 25.5
fbm_mean_1hdf5Display.SelectScaleArray = 'E'
fbm_mean_1hdf5Display.GlyphType = 'Arrow'
fbm_mean_1hdf5Display.GlyphTableIndexArray = 'E'
fbm_mean_1hdf5Display.GaussianRadius = 1.2750000000000001
fbm_mean_1hdf5Display.SetScaleArray = ['POINTS', 'E']
fbm_mean_1hdf5Display.ScaleTransferFunction = 'PiecewiseFunction'
fbm_mean_1hdf5Display.OpacityArray = ['POINTS', 'E']
fbm_mean_1hdf5Display.OpacityTransferFunction = 'PiecewiseFunction'
fbm_mean_1hdf5Display.DataAxesGrid = 'GridAxesRepresentation'
fbm_mean_1hdf5Display.SelectionCellLabelFontFile = ''
fbm_mean_1hdf5Display.SelectionPointLabelFontFile = ''
fbm_mean_1hdf5Display.PolarAxes = 'PolarAxesRepresentation'
fbm_mean_1hdf5Display.ScalarOpacityUnitDistance = 1.7320508075688774
fbm_mean_1hdf5Display.Slice = 127

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
fbm_mean_1hdf5Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5Display.DataAxesGrid.XTitleFontFile = ''
fbm_mean_1hdf5Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5Display.DataAxesGrid.YTitleFontFile = ''
fbm_mean_1hdf5Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5Display.DataAxesGrid.ZTitleFontFile = ''
fbm_mean_1hdf5Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5Display.DataAxesGrid.XLabelFontFile = ''
fbm_mean_1hdf5Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5Display.DataAxesGrid.YLabelFontFile = ''
fbm_mean_1hdf5Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
fbm_mean_1hdf5Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5Display.PolarAxes.PolarAxisTitleFontFile = ''
fbm_mean_1hdf5Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5Display.PolarAxes.PolarAxisLabelFontFile = ''
fbm_mean_1hdf5Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5Display.PolarAxes.LastRadialAxisTextFontFile = ''
fbm_mean_1hdf5Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(fbm_mean_1hdf5Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
fbm_mean_1hdf5Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
fbm_mean_1hdf5Display.SetScalarBarVisibility(renderView1, True)

# change representation type
fbm_mean_1hdf5Display.SetRepresentationType('Volume')

# current camera placement for renderView1
renderView1.CameraPosition = [543.5358867582902, 698.7981383075178, 605.5819902298207]
renderView1.CameraFocalPoint = [127.5, 127.5, 127.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 220.83647796503186

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/fbb/stats/h075/fbb_mean_256_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# hide data in view
Hide(fbm_mean_1hdf5, renderView1)

# create a new 'NetCDF Reader'
fbm_mean_1hdf5_1 = NetCDFReader(FileName=['/scratch/snx3000/klye/fbm/stats/H0_75/N128/fbm_mean_1.hdf5'])
fbm_mean_1hdf5_1.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# show data in view
fbm_mean_1hdf5_1Display = Show(fbm_mean_1hdf5_1, renderView1)

# trace defaults for the display properties.
fbm_mean_1hdf5_1Display.Representation = 'Outline'
fbm_mean_1hdf5_1Display.ColorArrayName = [None, '']
fbm_mean_1hdf5_1Display.OSPRayScaleArray = 'E'
fbm_mean_1hdf5_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
fbm_mean_1hdf5_1Display.SelectOrientationVectors = 'E'
fbm_mean_1hdf5_1Display.ScaleFactor = 12.700000000000001
fbm_mean_1hdf5_1Display.SelectScaleArray = 'E'
fbm_mean_1hdf5_1Display.GlyphType = 'Arrow'
fbm_mean_1hdf5_1Display.GlyphTableIndexArray = 'E'
fbm_mean_1hdf5_1Display.GaussianRadius = 0.635
fbm_mean_1hdf5_1Display.SetScaleArray = ['POINTS', 'E']
fbm_mean_1hdf5_1Display.ScaleTransferFunction = 'PiecewiseFunction'
fbm_mean_1hdf5_1Display.OpacityArray = ['POINTS', 'E']
fbm_mean_1hdf5_1Display.OpacityTransferFunction = 'PiecewiseFunction'
fbm_mean_1hdf5_1Display.DataAxesGrid = 'GridAxesRepresentation'
fbm_mean_1hdf5_1Display.SelectionCellLabelFontFile = ''
fbm_mean_1hdf5_1Display.SelectionPointLabelFontFile = ''
fbm_mean_1hdf5_1Display.PolarAxes = 'PolarAxesRepresentation'
fbm_mean_1hdf5_1Display.ScalarOpacityUnitDistance = 1.732050807568877
fbm_mean_1hdf5_1Display.Slice = 63

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
fbm_mean_1hdf5_1Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_1Display.DataAxesGrid.XTitleFontFile = ''
fbm_mean_1hdf5_1Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_1Display.DataAxesGrid.YTitleFontFile = ''
fbm_mean_1hdf5_1Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_1Display.DataAxesGrid.ZTitleFontFile = ''
fbm_mean_1hdf5_1Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_1Display.DataAxesGrid.XLabelFontFile = ''
fbm_mean_1hdf5_1Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_1Display.DataAxesGrid.YLabelFontFile = ''
fbm_mean_1hdf5_1Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
fbm_mean_1hdf5_1Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_1Display.PolarAxes.PolarAxisTitleFontFile = ''
fbm_mean_1hdf5_1Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_1Display.PolarAxes.PolarAxisLabelFontFile = ''
fbm_mean_1hdf5_1Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_1Display.PolarAxes.LastRadialAxisTextFontFile = ''
fbm_mean_1hdf5_1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(fbm_mean_1hdf5_1Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
fbm_mean_1hdf5_1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
fbm_mean_1hdf5_1Display.SetScalarBarVisibility(renderView1, True)

# change representation type
fbm_mean_1hdf5_1Display.SetRepresentationType('Volume')

# current camera placement for renderView1
renderView1.CameraPosition = [270.70218673844255, 348.0288767257049, 301.60357944779304]
renderView1.CameraFocalPoint = [63.5, 63.5, 63.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 109.9852262806237

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/fbb/stats/h075/fbb_mean_128_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
fbm_mean_1hdf5_2 = NetCDFReader(FileName=['/scratch/snx3000/klye/fbm/stats/H0_75/N64/fbm_mean_1.hdf5'])
fbm_mean_1hdf5_2.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(fbm_mean_1hdf5_1, renderView1)

# show data in view
fbm_mean_1hdf5_2Display = Show(fbm_mean_1hdf5_2, renderView1)

# trace defaults for the display properties.
fbm_mean_1hdf5_2Display.Representation = 'Outline'
fbm_mean_1hdf5_2Display.ColorArrayName = [None, '']
fbm_mean_1hdf5_2Display.OSPRayScaleArray = 'E'
fbm_mean_1hdf5_2Display.OSPRayScaleFunction = 'PiecewiseFunction'
fbm_mean_1hdf5_2Display.SelectOrientationVectors = 'E'
fbm_mean_1hdf5_2Display.ScaleFactor = 6.300000000000001
fbm_mean_1hdf5_2Display.SelectScaleArray = 'E'
fbm_mean_1hdf5_2Display.GlyphType = 'Arrow'
fbm_mean_1hdf5_2Display.GlyphTableIndexArray = 'E'
fbm_mean_1hdf5_2Display.GaussianRadius = 0.315
fbm_mean_1hdf5_2Display.SetScaleArray = ['POINTS', 'E']
fbm_mean_1hdf5_2Display.ScaleTransferFunction = 'PiecewiseFunction'
fbm_mean_1hdf5_2Display.OpacityArray = ['POINTS', 'E']
fbm_mean_1hdf5_2Display.OpacityTransferFunction = 'PiecewiseFunction'
fbm_mean_1hdf5_2Display.DataAxesGrid = 'GridAxesRepresentation'
fbm_mean_1hdf5_2Display.SelectionCellLabelFontFile = ''
fbm_mean_1hdf5_2Display.SelectionPointLabelFontFile = ''
fbm_mean_1hdf5_2Display.PolarAxes = 'PolarAxesRepresentation'
fbm_mean_1hdf5_2Display.ScalarOpacityUnitDistance = 1.7320508075688774
fbm_mean_1hdf5_2Display.Slice = 31

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
fbm_mean_1hdf5_2Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_2Display.DataAxesGrid.XTitleFontFile = ''
fbm_mean_1hdf5_2Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_2Display.DataAxesGrid.YTitleFontFile = ''
fbm_mean_1hdf5_2Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_2Display.DataAxesGrid.ZTitleFontFile = ''
fbm_mean_1hdf5_2Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_2Display.DataAxesGrid.XLabelFontFile = ''
fbm_mean_1hdf5_2Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_2Display.DataAxesGrid.YLabelFontFile = ''
fbm_mean_1hdf5_2Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_2Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
fbm_mean_1hdf5_2Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_2Display.PolarAxes.PolarAxisTitleFontFile = ''
fbm_mean_1hdf5_2Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_2Display.PolarAxes.PolarAxisLabelFontFile = ''
fbm_mean_1hdf5_2Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_2Display.PolarAxes.LastRadialAxisTextFontFile = ''
fbm_mean_1hdf5_2Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_mean_1hdf5_2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(fbm_mean_1hdf5_2Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
fbm_mean_1hdf5_2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
fbm_mean_1hdf5_2Display.SetScalarBarVisibility(renderView1, True)

# change representation type
fbm_mean_1hdf5_2Display.SetRepresentationType('Volume')

# current camera placement for renderView1
renderView1.CameraPosition = [134.28533672851876, 172.6442459347985, 149.61437405677924]
renderView1.CameraFocalPoint = [31.5, 31.5, 31.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 54.559600438419636

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/fbb/stats/h075/fbb_mean_64_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
fbm_variance_1hdf5 = NetCDFReader(FileName=['/scratch/snx3000/klye/fbm/stats/H0_75/N512/fbm_variance_1.hdf5'])
fbm_variance_1hdf5.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(fbm_mean_1hdf5_2, renderView1)

# set active source
SetActiveSource(fbm_variance_1hdf5)

# show data in view
fbm_variance_1hdf5Display = Show(fbm_variance_1hdf5, renderView1)

# trace defaults for the display properties.
fbm_variance_1hdf5Display.Representation = 'Outline'
fbm_variance_1hdf5Display.ColorArrayName = [None, '']
fbm_variance_1hdf5Display.OSPRayScaleArray = 'E'
fbm_variance_1hdf5Display.OSPRayScaleFunction = 'PiecewiseFunction'
fbm_variance_1hdf5Display.SelectOrientationVectors = 'E'
fbm_variance_1hdf5Display.ScaleFactor = 51.1
fbm_variance_1hdf5Display.SelectScaleArray = 'E'
fbm_variance_1hdf5Display.GlyphType = 'Arrow'
fbm_variance_1hdf5Display.GlyphTableIndexArray = 'E'
fbm_variance_1hdf5Display.GaussianRadius = 2.555
fbm_variance_1hdf5Display.SetScaleArray = ['POINTS', 'E']
fbm_variance_1hdf5Display.ScaleTransferFunction = 'PiecewiseFunction'
fbm_variance_1hdf5Display.OpacityArray = ['POINTS', 'E']
fbm_variance_1hdf5Display.OpacityTransferFunction = 'PiecewiseFunction'
fbm_variance_1hdf5Display.DataAxesGrid = 'GridAxesRepresentation'
fbm_variance_1hdf5Display.SelectionCellLabelFontFile = ''
fbm_variance_1hdf5Display.SelectionPointLabelFontFile = ''
fbm_variance_1hdf5Display.PolarAxes = 'PolarAxesRepresentation'
fbm_variance_1hdf5Display.ScalarOpacityUnitDistance = 1.732050807568877
fbm_variance_1hdf5Display.Slice = 255

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
fbm_variance_1hdf5Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5Display.DataAxesGrid.XTitleFontFile = ''
fbm_variance_1hdf5Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5Display.DataAxesGrid.YTitleFontFile = ''
fbm_variance_1hdf5Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5Display.DataAxesGrid.ZTitleFontFile = ''
fbm_variance_1hdf5Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5Display.DataAxesGrid.XLabelFontFile = ''
fbm_variance_1hdf5Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5Display.DataAxesGrid.YLabelFontFile = ''
fbm_variance_1hdf5Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
fbm_variance_1hdf5Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5Display.PolarAxes.PolarAxisTitleFontFile = ''
fbm_variance_1hdf5Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5Display.PolarAxes.PolarAxisLabelFontFile = ''
fbm_variance_1hdf5Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5Display.PolarAxes.LastRadialAxisTextFontFile = ''
fbm_variance_1hdf5Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# show data in view
fbm_variance_1hdf5Display = Show(fbm_variance_1hdf5, renderView1)

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(fbm_variance_1hdf5Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
fbm_variance_1hdf5Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
fbm_variance_1hdf5Display.SetScalarBarVisibility(renderView1, True)

# change representation type
fbm_variance_1hdf5Display.SetRepresentationType('Volume')

# rescale color and/or opacity maps used to exactly fit the current data range
fbm_variance_1hdf5Display.RescaleTransferFunctionToDataRange(False, True)

# Rescale transfer function
rhoLUT.RescaleTransferFunction(0.1, 0.2)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(0.1, 0.2)

# Rescale transfer function
rhoLUT.RescaleTransferFunction(0.05, 0.2)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(0.05, 0.2)

# Rescale transfer function
rhoLUT.RescaleTransferFunction(0.05, 0.15)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(0.05, 0.15)

# current camera placement for renderView1
renderView1.CameraPosition = [1089.2032867979854, 1400.3366614711433, 1213.538811793876]
renderView1.CameraFocalPoint = [255.5, 255.5, 255.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 442.53898133384814

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/fbb/stats/h075/fbb_variance_512_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# hide data in view
Hide(fbm_variance_1hdf5, renderView1)

# create a new 'NetCDF Reader'
fbm_variance_1hdf5_1 = NetCDFReader(FileName=['/scratch/snx3000/klye/fbm/stats/H0_75/N256/fbm_variance_1.hdf5'])
fbm_variance_1hdf5_1.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# show data in view
fbm_variance_1hdf5_1Display = Show(fbm_variance_1hdf5_1, renderView1)

# trace defaults for the display properties.
fbm_variance_1hdf5_1Display.Representation = 'Outline'
fbm_variance_1hdf5_1Display.ColorArrayName = [None, '']
fbm_variance_1hdf5_1Display.OSPRayScaleArray = 'E'
fbm_variance_1hdf5_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
fbm_variance_1hdf5_1Display.SelectOrientationVectors = 'E'
fbm_variance_1hdf5_1Display.ScaleFactor = 25.5
fbm_variance_1hdf5_1Display.SelectScaleArray = 'E'
fbm_variance_1hdf5_1Display.GlyphType = 'Arrow'
fbm_variance_1hdf5_1Display.GlyphTableIndexArray = 'E'
fbm_variance_1hdf5_1Display.GaussianRadius = 1.2750000000000001
fbm_variance_1hdf5_1Display.SetScaleArray = ['POINTS', 'E']
fbm_variance_1hdf5_1Display.ScaleTransferFunction = 'PiecewiseFunction'
fbm_variance_1hdf5_1Display.OpacityArray = ['POINTS', 'E']
fbm_variance_1hdf5_1Display.OpacityTransferFunction = 'PiecewiseFunction'
fbm_variance_1hdf5_1Display.DataAxesGrid = 'GridAxesRepresentation'
fbm_variance_1hdf5_1Display.SelectionCellLabelFontFile = ''
fbm_variance_1hdf5_1Display.SelectionPointLabelFontFile = ''
fbm_variance_1hdf5_1Display.PolarAxes = 'PolarAxesRepresentation'
fbm_variance_1hdf5_1Display.ScalarOpacityUnitDistance = 1.7320508075688774
fbm_variance_1hdf5_1Display.Slice = 127

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
fbm_variance_1hdf5_1Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_1Display.DataAxesGrid.XTitleFontFile = ''
fbm_variance_1hdf5_1Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_1Display.DataAxesGrid.YTitleFontFile = ''
fbm_variance_1hdf5_1Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_1Display.DataAxesGrid.ZTitleFontFile = ''
fbm_variance_1hdf5_1Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_1Display.DataAxesGrid.XLabelFontFile = ''
fbm_variance_1hdf5_1Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_1Display.DataAxesGrid.YLabelFontFile = ''
fbm_variance_1hdf5_1Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
fbm_variance_1hdf5_1Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_1Display.PolarAxes.PolarAxisTitleFontFile = ''
fbm_variance_1hdf5_1Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_1Display.PolarAxes.PolarAxisLabelFontFile = ''
fbm_variance_1hdf5_1Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_1Display.PolarAxes.LastRadialAxisTextFontFile = ''
fbm_variance_1hdf5_1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(fbm_variance_1hdf5_1Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
fbm_variance_1hdf5_1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
fbm_variance_1hdf5_1Display.SetScalarBarVisibility(renderView1, True)

# change representation type
fbm_variance_1hdf5_1Display.SetRepresentationType('Volume')

# Rescale transfer function
rhoLUT.RescaleTransferFunction(0.05, 0.15)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(0.05, 0.15)

# current camera placement for renderView1
renderView1.CameraPosition = [543.5358867582902, 698.7981383075178, 605.5819902298207]
renderView1.CameraFocalPoint = [127.5, 127.5, 127.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 220.83647796503186

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/fbb/stats/h075/fbb_variance_256_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
fbm_variance_1hdf5_2 = NetCDFReader(FileName=['/scratch/snx3000/klye/fbm/stats/H0_75/N128/fbm_variance_1.hdf5'])
fbm_variance_1hdf5_2.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(fbm_variance_1hdf5_1, renderView1)

# show data in view
fbm_variance_1hdf5_2Display = Show(fbm_variance_1hdf5_2, renderView1)

# trace defaults for the display properties.
fbm_variance_1hdf5_2Display.Representation = 'Outline'
fbm_variance_1hdf5_2Display.ColorArrayName = [None, '']
fbm_variance_1hdf5_2Display.OSPRayScaleArray = 'E'
fbm_variance_1hdf5_2Display.OSPRayScaleFunction = 'PiecewiseFunction'
fbm_variance_1hdf5_2Display.SelectOrientationVectors = 'E'
fbm_variance_1hdf5_2Display.ScaleFactor = 12.700000000000001
fbm_variance_1hdf5_2Display.SelectScaleArray = 'E'
fbm_variance_1hdf5_2Display.GlyphType = 'Arrow'
fbm_variance_1hdf5_2Display.GlyphTableIndexArray = 'E'
fbm_variance_1hdf5_2Display.GaussianRadius = 0.635
fbm_variance_1hdf5_2Display.SetScaleArray = ['POINTS', 'E']
fbm_variance_1hdf5_2Display.ScaleTransferFunction = 'PiecewiseFunction'
fbm_variance_1hdf5_2Display.OpacityArray = ['POINTS', 'E']
fbm_variance_1hdf5_2Display.OpacityTransferFunction = 'PiecewiseFunction'
fbm_variance_1hdf5_2Display.DataAxesGrid = 'GridAxesRepresentation'
fbm_variance_1hdf5_2Display.SelectionCellLabelFontFile = ''
fbm_variance_1hdf5_2Display.SelectionPointLabelFontFile = ''
fbm_variance_1hdf5_2Display.PolarAxes = 'PolarAxesRepresentation'
fbm_variance_1hdf5_2Display.ScalarOpacityUnitDistance = 1.732050807568877
fbm_variance_1hdf5_2Display.Slice = 63

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
fbm_variance_1hdf5_2Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_2Display.DataAxesGrid.XTitleFontFile = ''
fbm_variance_1hdf5_2Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_2Display.DataAxesGrid.YTitleFontFile = ''
fbm_variance_1hdf5_2Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_2Display.DataAxesGrid.ZTitleFontFile = ''
fbm_variance_1hdf5_2Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_2Display.DataAxesGrid.XLabelFontFile = ''
fbm_variance_1hdf5_2Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_2Display.DataAxesGrid.YLabelFontFile = ''
fbm_variance_1hdf5_2Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_2Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
fbm_variance_1hdf5_2Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_2Display.PolarAxes.PolarAxisTitleFontFile = ''
fbm_variance_1hdf5_2Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_2Display.PolarAxes.PolarAxisLabelFontFile = ''
fbm_variance_1hdf5_2Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_2Display.PolarAxes.LastRadialAxisTextFontFile = ''
fbm_variance_1hdf5_2Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(fbm_variance_1hdf5_2Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
fbm_variance_1hdf5_2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
fbm_variance_1hdf5_2Display.SetScalarBarVisibility(renderView1, True)

# change representation type
fbm_variance_1hdf5_2Display.SetRepresentationType('Volume')

# Rescale transfer function
rhoLUT.RescaleTransferFunction(0.05, 0.15)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(0.05, 0.15)

# current camera placement for renderView1
renderView1.CameraPosition = [270.70218673844255, 348.0288767257049, 301.60357944779304]
renderView1.CameraFocalPoint = [63.5, 63.5, 63.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 109.9852262806237

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/fbb/stats/h075/fbb_variance_128_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
fbm_variance_1hdf5_3 = NetCDFReader(FileName=['/scratch/snx3000/klye/fbm/stats/H0_75/N64/fbm_variance_1.hdf5'])
fbm_variance_1hdf5_3.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(fbm_variance_1hdf5_2, renderView1)

# show data in view
fbm_variance_1hdf5_3Display = Show(fbm_variance_1hdf5_3, renderView1)

# trace defaults for the display properties.
fbm_variance_1hdf5_3Display.Representation = 'Outline'
fbm_variance_1hdf5_3Display.ColorArrayName = [None, '']
fbm_variance_1hdf5_3Display.OSPRayScaleArray = 'E'
fbm_variance_1hdf5_3Display.OSPRayScaleFunction = 'PiecewiseFunction'
fbm_variance_1hdf5_3Display.SelectOrientationVectors = 'E'
fbm_variance_1hdf5_3Display.ScaleFactor = 6.300000000000001
fbm_variance_1hdf5_3Display.SelectScaleArray = 'E'
fbm_variance_1hdf5_3Display.GlyphType = 'Arrow'
fbm_variance_1hdf5_3Display.GlyphTableIndexArray = 'E'
fbm_variance_1hdf5_3Display.GaussianRadius = 0.315
fbm_variance_1hdf5_3Display.SetScaleArray = ['POINTS', 'E']
fbm_variance_1hdf5_3Display.ScaleTransferFunction = 'PiecewiseFunction'
fbm_variance_1hdf5_3Display.OpacityArray = ['POINTS', 'E']
fbm_variance_1hdf5_3Display.OpacityTransferFunction = 'PiecewiseFunction'
fbm_variance_1hdf5_3Display.DataAxesGrid = 'GridAxesRepresentation'
fbm_variance_1hdf5_3Display.SelectionCellLabelFontFile = ''
fbm_variance_1hdf5_3Display.SelectionPointLabelFontFile = ''
fbm_variance_1hdf5_3Display.PolarAxes = 'PolarAxesRepresentation'
fbm_variance_1hdf5_3Display.ScalarOpacityUnitDistance = 1.7320508075688774
fbm_variance_1hdf5_3Display.Slice = 31

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
fbm_variance_1hdf5_3Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_3Display.DataAxesGrid.XTitleFontFile = ''
fbm_variance_1hdf5_3Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_3Display.DataAxesGrid.YTitleFontFile = ''
fbm_variance_1hdf5_3Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_3Display.DataAxesGrid.ZTitleFontFile = ''
fbm_variance_1hdf5_3Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_3Display.DataAxesGrid.XLabelFontFile = ''
fbm_variance_1hdf5_3Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_3Display.DataAxesGrid.YLabelFontFile = ''
fbm_variance_1hdf5_3Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_3Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
fbm_variance_1hdf5_3Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_3Display.PolarAxes.PolarAxisTitleFontFile = ''
fbm_variance_1hdf5_3Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_3Display.PolarAxes.PolarAxisLabelFontFile = ''
fbm_variance_1hdf5_3Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_3Display.PolarAxes.LastRadialAxisTextFontFile = ''
fbm_variance_1hdf5_3Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_variance_1hdf5_3Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(fbm_variance_1hdf5_3Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
fbm_variance_1hdf5_3Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
fbm_variance_1hdf5_3Display.SetScalarBarVisibility(renderView1, True)

# change representation type
fbm_variance_1hdf5_3Display.SetRepresentationType('Volume')

# Rescale transfer function
rhoLUT.RescaleTransferFunction(0.05, 0.15)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(0.05, 0.15)

# current camera placement for renderView1
renderView1.CameraPosition = [134.28533672851876, 172.6442459347985, 149.61437405677924]
renderView1.CameraFocalPoint = [31.5, 31.5, 31.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 54.559600438419636

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/fbb/stats/h075/fbb_variance_64_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# hide data in view
Hide(fbm_variance_1hdf5_3, renderView1)

# set active source
SetActiveSource(fbm_variance_1hdf5_3)

# show data in view
fbm_variance_1hdf5_3Display = Show(fbm_variance_1hdf5_3, renderView1)

# show color bar/color legend
fbm_variance_1hdf5_3Display.SetScalarBarVisibility(renderView1, True)

# reset view to fit data
renderView1.ResetCamera()

# hide data in view
Hide(fbm_variance_1hdf5_3, renderView1)

# create a new 'NetCDF Reader'
fbm_1hdf5 = NetCDFReader(FileName=['/scratch/snx3000/klye/fbm/single/H0_1/N512/fbm_1.hdf5'])
fbm_1hdf5.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# show data in view
fbm_1hdf5Display = Show(fbm_1hdf5, renderView1)

# trace defaults for the display properties.
fbm_1hdf5Display.Representation = 'Outline'
fbm_1hdf5Display.ColorArrayName = [None, '']
fbm_1hdf5Display.OSPRayScaleArray = 'sample_0_E'
fbm_1hdf5Display.OSPRayScaleFunction = 'PiecewiseFunction'
fbm_1hdf5Display.SelectOrientationVectors = 'None'
fbm_1hdf5Display.ScaleFactor = 51.1
fbm_1hdf5Display.SelectScaleArray = 'None'
fbm_1hdf5Display.GlyphType = 'Arrow'
fbm_1hdf5Display.GlyphTableIndexArray = 'None'
fbm_1hdf5Display.GaussianRadius = 2.555
fbm_1hdf5Display.SetScaleArray = ['POINTS', 'sample_0_E']
fbm_1hdf5Display.ScaleTransferFunction = 'PiecewiseFunction'
fbm_1hdf5Display.OpacityArray = ['POINTS', 'sample_0_E']
fbm_1hdf5Display.OpacityTransferFunction = 'PiecewiseFunction'
fbm_1hdf5Display.DataAxesGrid = 'GridAxesRepresentation'
fbm_1hdf5Display.SelectionCellLabelFontFile = ''
fbm_1hdf5Display.SelectionPointLabelFontFile = ''
fbm_1hdf5Display.PolarAxes = 'PolarAxesRepresentation'
fbm_1hdf5Display.ScalarOpacityUnitDistance = 1.732050807568877
fbm_1hdf5Display.Slice = 255

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
fbm_1hdf5Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5Display.DataAxesGrid.XTitleFontFile = ''
fbm_1hdf5Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5Display.DataAxesGrid.YTitleFontFile = ''
fbm_1hdf5Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5Display.DataAxesGrid.ZTitleFontFile = ''
fbm_1hdf5Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5Display.DataAxesGrid.XLabelFontFile = ''
fbm_1hdf5Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5Display.DataAxesGrid.YLabelFontFile = ''
fbm_1hdf5Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
fbm_1hdf5Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5Display.PolarAxes.PolarAxisTitleFontFile = ''
fbm_1hdf5Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5Display.PolarAxes.PolarAxisLabelFontFile = ''
fbm_1hdf5Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5Display.PolarAxes.LastRadialAxisTextFontFile = ''
fbm_1hdf5Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(fbm_mean_1hdf5_4)

# destroy fbm_mean_1hdf5_4
Delete(fbm_mean_1hdf5_4)
del fbm_mean_1hdf5_4

# set active source
SetActiveSource(fbm_mean_1hdf5)

# destroy fbm_mean_1hdf5
Delete(fbm_mean_1hdf5)
del fbm_mean_1hdf5

# set active source
SetActiveSource(fbm_mean_1hdf5_1)

# destroy fbm_mean_1hdf5_1
Delete(fbm_mean_1hdf5_1)
del fbm_mean_1hdf5_1

# set active source
SetActiveSource(fbm_mean_1hdf5_2)

# destroy fbm_mean_1hdf5_2
Delete(fbm_mean_1hdf5_2)
del fbm_mean_1hdf5_2

# set active source
SetActiveSource(fbm_variance_1hdf5)

# destroy fbm_variance_1hdf5
Delete(fbm_variance_1hdf5)
del fbm_variance_1hdf5

# set active source
SetActiveSource(fbm_variance_1hdf5_1)

# destroy fbm_variance_1hdf5_1
Delete(fbm_variance_1hdf5_1)
del fbm_variance_1hdf5_1

# set active source
SetActiveSource(fbm_variance_1hdf5_2)

# destroy fbm_variance_1hdf5_2
Delete(fbm_variance_1hdf5_2)
del fbm_variance_1hdf5_2

# set active source
SetActiveSource(fbm_variance_1hdf5_3)

# destroy fbm_variance_1hdf5_3
Delete(fbm_variance_1hdf5_3)
del fbm_variance_1hdf5_3

# set active source
SetActiveSource(fbm_1hdf5)

# set scalar coloring
ColorBy(fbm_1hdf5Display, ('POINTS', 'sample_0_rho'))

# rescale color and/or opacity maps used to include current data range
fbm_1hdf5Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
fbm_1hdf5Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'sample_0_rho'
sample_0_rhoLUT = GetColorTransferFunction('sample_0_rho')
sample_0_rhoLUT.RGBPoints = [0.9997859001159668, 0.231373, 0.298039, 0.752941, 8.687084913253784, 0.865003, 0.865003, 0.865003, 16.3743839263916, 0.705882, 0.0156863, 0.14902]
sample_0_rhoLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'sample_0_rho'
sample_0_rhoPWF = GetOpacityTransferFunction('sample_0_rho')
sample_0_rhoPWF.Points = [0.9997859001159668, 0.0, 0.5, 0.0, 16.3743839263916, 1.0, 0.5, 0.0]
sample_0_rhoPWF.ScalarRangeInitialized = 1

# change representation type
fbm_1hdf5Display.SetRepresentationType('Volume')

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
sample_0_rhoLUT.ApplyPreset('Viridis (matplotlib)', True)

# rescale color and/or opacity maps used to exactly fit the current data range
fbm_1hdf5Display.RescaleTransferFunctionToDataRange(False, True)

# Rescale transfer function
sample_0_rhoLUT.RescaleTransferFunction(1.0, 12.0)

# Rescale transfer function
sample_0_rhoPWF.RescaleTransferFunction(1.0, 12.0)

# rescale color and/or opacity maps used to exactly fit the current data range
fbm_1hdf5Display.RescaleTransferFunctionToDataRange(False, True)

# Rescale transfer function
sample_0_rhoLUT.RescaleTransferFunction(1.0, 10.0)

# Rescale transfer function
sample_0_rhoPWF.RescaleTransferFunction(1.0, 10.0)

# current camera placement for renderView1
renderView1.CameraPosition = [1089.2032867979854, 1400.3366614711433, 1213.538811793876]
renderView1.CameraFocalPoint = [255.5, 255.5, 255.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 442.53898133384814

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/fbb/single/h01/fbb_single_512_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
fbm_1hdf5_1 = NetCDFReader(FileName=['/scratch/snx3000/klye/fbm/single/H0_1/N256/fbm_1.hdf5'])
fbm_1hdf5_1.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# show data in view
fbm_1hdf5_1Display = Show(fbm_1hdf5_1, renderView1)

# trace defaults for the display properties.
fbm_1hdf5_1Display.Representation = 'Outline'
fbm_1hdf5_1Display.ColorArrayName = [None, '']
fbm_1hdf5_1Display.OSPRayScaleArray = 'sample_0_E'
fbm_1hdf5_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
fbm_1hdf5_1Display.SelectOrientationVectors = 'None'
fbm_1hdf5_1Display.ScaleFactor = 25.5
fbm_1hdf5_1Display.SelectScaleArray = 'None'
fbm_1hdf5_1Display.GlyphType = 'Arrow'
fbm_1hdf5_1Display.GlyphTableIndexArray = 'None'
fbm_1hdf5_1Display.GaussianRadius = 1.2750000000000001
fbm_1hdf5_1Display.SetScaleArray = ['POINTS', 'sample_0_E']
fbm_1hdf5_1Display.ScaleTransferFunction = 'PiecewiseFunction'
fbm_1hdf5_1Display.OpacityArray = ['POINTS', 'sample_0_E']
fbm_1hdf5_1Display.OpacityTransferFunction = 'PiecewiseFunction'
fbm_1hdf5_1Display.DataAxesGrid = 'GridAxesRepresentation'
fbm_1hdf5_1Display.SelectionCellLabelFontFile = ''
fbm_1hdf5_1Display.SelectionPointLabelFontFile = ''
fbm_1hdf5_1Display.PolarAxes = 'PolarAxesRepresentation'
fbm_1hdf5_1Display.ScalarOpacityUnitDistance = 1.7320508075688774
fbm_1hdf5_1Display.Slice = 127

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
fbm_1hdf5_1Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_1Display.DataAxesGrid.XTitleFontFile = ''
fbm_1hdf5_1Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_1Display.DataAxesGrid.YTitleFontFile = ''
fbm_1hdf5_1Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_1Display.DataAxesGrid.ZTitleFontFile = ''
fbm_1hdf5_1Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_1Display.DataAxesGrid.XLabelFontFile = ''
fbm_1hdf5_1Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_1Display.DataAxesGrid.YLabelFontFile = ''
fbm_1hdf5_1Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
fbm_1hdf5_1Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_1Display.PolarAxes.PolarAxisTitleFontFile = ''
fbm_1hdf5_1Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_1Display.PolarAxes.PolarAxisLabelFontFile = ''
fbm_1hdf5_1Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_1Display.PolarAxes.LastRadialAxisTextFontFile = ''
fbm_1hdf5_1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# update the view to ensure updated data information
renderView1.Update()

# Rescale transfer function
sample_0_rhoLUT.RescaleTransferFunction(0.999785900116, 16.3743839264)

# Rescale transfer function
sample_0_rhoPWF.RescaleTransferFunction(0.999785900116, 16.3743839264)

# hide data in view
Hide(fbm_1hdf5, renderView1)

# set scalar coloring
ColorBy(fbm_1hdf5_1Display, ('POINTS', 'sample_0_rho'))

# rescale color and/or opacity maps used to include current data range
fbm_1hdf5_1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
fbm_1hdf5_1Display.SetScalarBarVisibility(renderView1, True)

# change representation type
fbm_1hdf5_1Display.SetRepresentationType('Volume')

# hide data in view
Hide(fbm_1hdf5_1, renderView1)

# set active source
SetActiveSource(fbm_1hdf5_1)

# show data in view
fbm_1hdf5_1Display = Show(fbm_1hdf5_1, renderView1)

# show color bar/color legend
fbm_1hdf5_1Display.SetScalarBarVisibility(renderView1, True)

# reset view to fit data
renderView1.ResetCamera()

# Rescale transfer function
sample_0_rhoLUT.RescaleTransferFunction(1.0, 10.0)

# Rescale transfer function
sample_0_rhoPWF.RescaleTransferFunction(1.0, 10.0)

# current camera placement for renderView1
renderView1.CameraPosition = [543.5358867582902, 698.7981383075178, 605.5819902298207]
renderView1.CameraFocalPoint = [127.5, 127.5, 127.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 220.83647796503186

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/fbb/single/h01/fbb_single_256_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
fbm_1hdf5_2 = NetCDFReader(FileName=['/scratch/snx3000/klye/fbm/single/H0_1/N128/fbm_1.hdf5'])
fbm_1hdf5_2.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(fbm_1hdf5_1, renderView1)

# set active source
SetActiveSource(fbm_1hdf5_2)

# show data in view
fbm_1hdf5_2Display = Show(fbm_1hdf5_2, renderView1)

# trace defaults for the display properties.
fbm_1hdf5_2Display.Representation = 'Outline'
fbm_1hdf5_2Display.ColorArrayName = [None, '']
fbm_1hdf5_2Display.OSPRayScaleArray = 'sample_0_E'
fbm_1hdf5_2Display.OSPRayScaleFunction = 'PiecewiseFunction'
fbm_1hdf5_2Display.SelectOrientationVectors = 'None'
fbm_1hdf5_2Display.ScaleFactor = 12.700000000000001
fbm_1hdf5_2Display.SelectScaleArray = 'None'
fbm_1hdf5_2Display.GlyphType = 'Arrow'
fbm_1hdf5_2Display.GlyphTableIndexArray = 'None'
fbm_1hdf5_2Display.GaussianRadius = 0.635
fbm_1hdf5_2Display.SetScaleArray = ['POINTS', 'sample_0_E']
fbm_1hdf5_2Display.ScaleTransferFunction = 'PiecewiseFunction'
fbm_1hdf5_2Display.OpacityArray = ['POINTS', 'sample_0_E']
fbm_1hdf5_2Display.OpacityTransferFunction = 'PiecewiseFunction'
fbm_1hdf5_2Display.DataAxesGrid = 'GridAxesRepresentation'
fbm_1hdf5_2Display.SelectionCellLabelFontFile = ''
fbm_1hdf5_2Display.SelectionPointLabelFontFile = ''
fbm_1hdf5_2Display.PolarAxes = 'PolarAxesRepresentation'
fbm_1hdf5_2Display.ScalarOpacityUnitDistance = 1.732050807568877
fbm_1hdf5_2Display.Slice = 63

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
fbm_1hdf5_2Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_2Display.DataAxesGrid.XTitleFontFile = ''
fbm_1hdf5_2Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_2Display.DataAxesGrid.YTitleFontFile = ''
fbm_1hdf5_2Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_2Display.DataAxesGrid.ZTitleFontFile = ''
fbm_1hdf5_2Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_2Display.DataAxesGrid.XLabelFontFile = ''
fbm_1hdf5_2Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_2Display.DataAxesGrid.YLabelFontFile = ''
fbm_1hdf5_2Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_2Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
fbm_1hdf5_2Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_2Display.PolarAxes.PolarAxisTitleFontFile = ''
fbm_1hdf5_2Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_2Display.PolarAxes.PolarAxisLabelFontFile = ''
fbm_1hdf5_2Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_2Display.PolarAxes.LastRadialAxisTextFontFile = ''
fbm_1hdf5_2Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# set scalar coloring
ColorBy(fbm_1hdf5_2Display, ('POINTS', 'sample_0_rho'))

# rescale color and/or opacity maps used to include current data range
fbm_1hdf5_2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
fbm_1hdf5_2Display.SetScalarBarVisibility(renderView1, True)

# change representation type
fbm_1hdf5_2Display.SetRepresentationType('Volume')

# Rescale transfer function
sample_0_rhoLUT.RescaleTransferFunction(1.0, 10.0)

# Rescale transfer function
sample_0_rhoPWF.RescaleTransferFunction(1.0, 10.0)

# current camera placement for renderView1
renderView1.CameraPosition = [270.70218673844255, 348.0288767257049, 301.60357944779304]
renderView1.CameraFocalPoint = [63.5, 63.5, 63.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 109.9852262806237

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/fbb/single/h01/fbb_single_128_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
fbm_1hdf5_3 = NetCDFReader(FileName=['/scratch/snx3000/klye/fbm/single/H0_1/N64/fbm_1.hdf5'])
fbm_1hdf5_3.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(fbm_1hdf5_2, renderView1)

# show data in view
fbm_1hdf5_3Display = Show(fbm_1hdf5_3, renderView1)

# trace defaults for the display properties.
fbm_1hdf5_3Display.Representation = 'Outline'
fbm_1hdf5_3Display.ColorArrayName = [None, '']
fbm_1hdf5_3Display.OSPRayScaleArray = 'sample_0_E'
fbm_1hdf5_3Display.OSPRayScaleFunction = 'PiecewiseFunction'
fbm_1hdf5_3Display.SelectOrientationVectors = 'None'
fbm_1hdf5_3Display.ScaleFactor = 6.300000000000001
fbm_1hdf5_3Display.SelectScaleArray = 'None'
fbm_1hdf5_3Display.GlyphType = 'Arrow'
fbm_1hdf5_3Display.GlyphTableIndexArray = 'None'
fbm_1hdf5_3Display.GaussianRadius = 0.315
fbm_1hdf5_3Display.SetScaleArray = ['POINTS', 'sample_0_E']
fbm_1hdf5_3Display.ScaleTransferFunction = 'PiecewiseFunction'
fbm_1hdf5_3Display.OpacityArray = ['POINTS', 'sample_0_E']
fbm_1hdf5_3Display.OpacityTransferFunction = 'PiecewiseFunction'
fbm_1hdf5_3Display.DataAxesGrid = 'GridAxesRepresentation'
fbm_1hdf5_3Display.SelectionCellLabelFontFile = ''
fbm_1hdf5_3Display.SelectionPointLabelFontFile = ''
fbm_1hdf5_3Display.PolarAxes = 'PolarAxesRepresentation'
fbm_1hdf5_3Display.ScalarOpacityUnitDistance = 1.7320508075688774
fbm_1hdf5_3Display.Slice = 31

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
fbm_1hdf5_3Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_3Display.DataAxesGrid.XTitleFontFile = ''
fbm_1hdf5_3Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_3Display.DataAxesGrid.YTitleFontFile = ''
fbm_1hdf5_3Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_3Display.DataAxesGrid.ZTitleFontFile = ''
fbm_1hdf5_3Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_3Display.DataAxesGrid.XLabelFontFile = ''
fbm_1hdf5_3Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_3Display.DataAxesGrid.YLabelFontFile = ''
fbm_1hdf5_3Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_3Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
fbm_1hdf5_3Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_3Display.PolarAxes.PolarAxisTitleFontFile = ''
fbm_1hdf5_3Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_3Display.PolarAxes.PolarAxisLabelFontFile = ''
fbm_1hdf5_3Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_3Display.PolarAxes.LastRadialAxisTextFontFile = ''
fbm_1hdf5_3Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_3Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# show data in view
fbm_1hdf5_2Display = Show(fbm_1hdf5_2, renderView1)

# show color bar/color legend
fbm_1hdf5_2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# Rescale transfer function
sample_0_rhoLUT.RescaleTransferFunction(1.0, 12.3453130722)

# Rescale transfer function
sample_0_rhoPWF.RescaleTransferFunction(1.0, 12.3453130722)

# hide data in view
Hide(fbm_1hdf5_2, renderView1)

# hide data in view
Hide(fbm_1hdf5_3, renderView1)

# set active source
SetActiveSource(fbm_1hdf5_3)

# show data in view
fbm_1hdf5_3Display = Show(fbm_1hdf5_3, renderView1)

# reset view to fit data
renderView1.ResetCamera()

# set scalar coloring
ColorBy(fbm_1hdf5_3Display, ('POINTS', 'sample_0_rho'))

# rescale color and/or opacity maps used to include current data range
fbm_1hdf5_3Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
fbm_1hdf5_3Display.SetScalarBarVisibility(renderView1, True)

# change representation type
fbm_1hdf5_3Display.SetRepresentationType('Volume')

# Rescale transfer function
sample_0_rhoLUT.RescaleTransferFunction(1.0, 10.0)

# Rescale transfer function
sample_0_rhoPWF.RescaleTransferFunction(1.0, 10.0)

# current camera placement for renderView1
renderView1.CameraPosition = [134.28533672851876, 172.6442459347985, 149.61437405677924]
renderView1.CameraFocalPoint = [31.5, 31.5, 31.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 54.559600438419636

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/fbb/single/h01/fbb_single_64_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
fbm_1hdf5_4 = NetCDFReader(FileName=['/scratch/snx3000/klye/fbm/single/H0_75/N512/fbm_1.hdf5'])
fbm_1hdf5_4.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(fbm_1hdf5_3, renderView1)

# show data in view
fbm_1hdf5_4Display = Show(fbm_1hdf5_4, renderView1)

# trace defaults for the display properties.
fbm_1hdf5_4Display.Representation = 'Outline'
fbm_1hdf5_4Display.ColorArrayName = [None, '']
fbm_1hdf5_4Display.OSPRayScaleArray = 'sample_0_E'
fbm_1hdf5_4Display.OSPRayScaleFunction = 'PiecewiseFunction'
fbm_1hdf5_4Display.SelectOrientationVectors = 'None'
fbm_1hdf5_4Display.ScaleFactor = 51.1
fbm_1hdf5_4Display.SelectScaleArray = 'None'
fbm_1hdf5_4Display.GlyphType = 'Arrow'
fbm_1hdf5_4Display.GlyphTableIndexArray = 'None'
fbm_1hdf5_4Display.GaussianRadius = 2.555
fbm_1hdf5_4Display.SetScaleArray = ['POINTS', 'sample_0_E']
fbm_1hdf5_4Display.ScaleTransferFunction = 'PiecewiseFunction'
fbm_1hdf5_4Display.OpacityArray = ['POINTS', 'sample_0_E']
fbm_1hdf5_4Display.OpacityTransferFunction = 'PiecewiseFunction'
fbm_1hdf5_4Display.DataAxesGrid = 'GridAxesRepresentation'
fbm_1hdf5_4Display.SelectionCellLabelFontFile = ''
fbm_1hdf5_4Display.SelectionPointLabelFontFile = ''
fbm_1hdf5_4Display.PolarAxes = 'PolarAxesRepresentation'
fbm_1hdf5_4Display.ScalarOpacityUnitDistance = 1.732050807568877
fbm_1hdf5_4Display.Slice = 255

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
fbm_1hdf5_4Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_4Display.DataAxesGrid.XTitleFontFile = ''
fbm_1hdf5_4Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_4Display.DataAxesGrid.YTitleFontFile = ''
fbm_1hdf5_4Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_4Display.DataAxesGrid.ZTitleFontFile = ''
fbm_1hdf5_4Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_4Display.DataAxesGrid.XLabelFontFile = ''
fbm_1hdf5_4Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_4Display.DataAxesGrid.YLabelFontFile = ''
fbm_1hdf5_4Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_4Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
fbm_1hdf5_4Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_4Display.PolarAxes.PolarAxisTitleFontFile = ''
fbm_1hdf5_4Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_4Display.PolarAxes.PolarAxisLabelFontFile = ''
fbm_1hdf5_4Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_4Display.PolarAxes.LastRadialAxisTextFontFile = ''
fbm_1hdf5_4Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_4Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(fbm_1hdf5_4Display, ('POINTS', 'sample_0_rho'))

# rescale color and/or opacity maps used to include current data range
fbm_1hdf5_4Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
fbm_1hdf5_4Display.SetScalarBarVisibility(renderView1, True)

# change representation type
fbm_1hdf5_4Display.SetRepresentationType('Volume')

# rescale color and/or opacity maps used to exactly fit the current data range
fbm_1hdf5_4Display.RescaleTransferFunctionToDataRange(False, True)

# Rescale transfer function
sample_0_rhoLUT.RescaleTransferFunction(2.5, 5.2)

# Rescale transfer function
sample_0_rhoPWF.RescaleTransferFunction(2.5, 5.2)

# current camera placement for renderView1
renderView1.CameraPosition = [1089.2032867979854, 1400.3366614711433, 1213.538811793876]
renderView1.CameraFocalPoint = [255.5, 255.5, 255.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 442.53898133384814

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/fbb/single/h075/fbb_single_512_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
fbm_1hdf5_5 = NetCDFReader(FileName=['/scratch/snx3000/klye/fbm/single/H0_75/N256/fbm_1.hdf5'])
fbm_1hdf5_5.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(fbm_1hdf5_4, renderView1)

# show data in view
fbm_1hdf5_5Display = Show(fbm_1hdf5_5, renderView1)

# trace defaults for the display properties.
fbm_1hdf5_5Display.Representation = 'Outline'
fbm_1hdf5_5Display.ColorArrayName = [None, '']
fbm_1hdf5_5Display.OSPRayScaleArray = 'sample_0_E'
fbm_1hdf5_5Display.OSPRayScaleFunction = 'PiecewiseFunction'
fbm_1hdf5_5Display.SelectOrientationVectors = 'None'
fbm_1hdf5_5Display.ScaleFactor = 25.5
fbm_1hdf5_5Display.SelectScaleArray = 'None'
fbm_1hdf5_5Display.GlyphType = 'Arrow'
fbm_1hdf5_5Display.GlyphTableIndexArray = 'None'
fbm_1hdf5_5Display.GaussianRadius = 1.2750000000000001
fbm_1hdf5_5Display.SetScaleArray = ['POINTS', 'sample_0_E']
fbm_1hdf5_5Display.ScaleTransferFunction = 'PiecewiseFunction'
fbm_1hdf5_5Display.OpacityArray = ['POINTS', 'sample_0_E']
fbm_1hdf5_5Display.OpacityTransferFunction = 'PiecewiseFunction'
fbm_1hdf5_5Display.DataAxesGrid = 'GridAxesRepresentation'
fbm_1hdf5_5Display.SelectionCellLabelFontFile = ''
fbm_1hdf5_5Display.SelectionPointLabelFontFile = ''
fbm_1hdf5_5Display.PolarAxes = 'PolarAxesRepresentation'
fbm_1hdf5_5Display.ScalarOpacityUnitDistance = 1.7320508075688774
fbm_1hdf5_5Display.Slice = 127

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
fbm_1hdf5_5Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_5Display.DataAxesGrid.XTitleFontFile = ''
fbm_1hdf5_5Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_5Display.DataAxesGrid.YTitleFontFile = ''
fbm_1hdf5_5Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_5Display.DataAxesGrid.ZTitleFontFile = ''
fbm_1hdf5_5Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_5Display.DataAxesGrid.XLabelFontFile = ''
fbm_1hdf5_5Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_5Display.DataAxesGrid.YLabelFontFile = ''
fbm_1hdf5_5Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_5Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
fbm_1hdf5_5Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_5Display.PolarAxes.PolarAxisTitleFontFile = ''
fbm_1hdf5_5Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_5Display.PolarAxes.PolarAxisLabelFontFile = ''
fbm_1hdf5_5Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_5Display.PolarAxes.LastRadialAxisTextFontFile = ''
fbm_1hdf5_5Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_5Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(fbm_1hdf5_5Display, ('POINTS', 'sample_0_rho'))

# rescale color and/or opacity maps used to include current data range
fbm_1hdf5_5Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
fbm_1hdf5_5Display.SetScalarBarVisibility(renderView1, True)

# change representation type
fbm_1hdf5_5Display.SetRepresentationType('Volume')

# Rescale transfer function
sample_0_rhoLUT.RescaleTransferFunction(2.5, 5.2)

# Rescale transfer function
sample_0_rhoPWF.RescaleTransferFunction(2.5, 5.2)

# current camera placement for renderView1
renderView1.CameraPosition = [543.5358867582902, 698.7981383075178, 605.5819902298207]
renderView1.CameraFocalPoint = [127.5, 127.5, 127.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 220.83647796503186

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/fbb/single/h075/fbb_single_256_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# hide data in view
Hide(fbm_1hdf5_5, renderView1)

# create a new 'NetCDF Reader'
fbm_1hdf5_6 = NetCDFReader(FileName=['/scratch/snx3000/klye/fbm/single/H0_75/N128/fbm_1.hdf5'])
fbm_1hdf5_6.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# show data in view
fbm_1hdf5_6Display = Show(fbm_1hdf5_6, renderView1)

# trace defaults for the display properties.
fbm_1hdf5_6Display.Representation = 'Outline'
fbm_1hdf5_6Display.ColorArrayName = [None, '']
fbm_1hdf5_6Display.OSPRayScaleArray = 'sample_0_E'
fbm_1hdf5_6Display.OSPRayScaleFunction = 'PiecewiseFunction'
fbm_1hdf5_6Display.SelectOrientationVectors = 'None'
fbm_1hdf5_6Display.ScaleFactor = 12.700000000000001
fbm_1hdf5_6Display.SelectScaleArray = 'None'
fbm_1hdf5_6Display.GlyphType = 'Arrow'
fbm_1hdf5_6Display.GlyphTableIndexArray = 'None'
fbm_1hdf5_6Display.GaussianRadius = 0.635
fbm_1hdf5_6Display.SetScaleArray = ['POINTS', 'sample_0_E']
fbm_1hdf5_6Display.ScaleTransferFunction = 'PiecewiseFunction'
fbm_1hdf5_6Display.OpacityArray = ['POINTS', 'sample_0_E']
fbm_1hdf5_6Display.OpacityTransferFunction = 'PiecewiseFunction'
fbm_1hdf5_6Display.DataAxesGrid = 'GridAxesRepresentation'
fbm_1hdf5_6Display.SelectionCellLabelFontFile = ''
fbm_1hdf5_6Display.SelectionPointLabelFontFile = ''
fbm_1hdf5_6Display.PolarAxes = 'PolarAxesRepresentation'
fbm_1hdf5_6Display.ScalarOpacityUnitDistance = 1.732050807568877
fbm_1hdf5_6Display.Slice = 63

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
fbm_1hdf5_6Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_6Display.DataAxesGrid.XTitleFontFile = ''
fbm_1hdf5_6Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_6Display.DataAxesGrid.YTitleFontFile = ''
fbm_1hdf5_6Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_6Display.DataAxesGrid.ZTitleFontFile = ''
fbm_1hdf5_6Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_6Display.DataAxesGrid.XLabelFontFile = ''
fbm_1hdf5_6Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_6Display.DataAxesGrid.YLabelFontFile = ''
fbm_1hdf5_6Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_6Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
fbm_1hdf5_6Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_6Display.PolarAxes.PolarAxisTitleFontFile = ''
fbm_1hdf5_6Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_6Display.PolarAxes.PolarAxisLabelFontFile = ''
fbm_1hdf5_6Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_6Display.PolarAxes.LastRadialAxisTextFontFile = ''
fbm_1hdf5_6Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_6Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(fbm_1hdf5_6Display, ('POINTS', 'sample_0_rho'))

# rescale color and/or opacity maps used to include current data range
fbm_1hdf5_6Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
fbm_1hdf5_6Display.SetScalarBarVisibility(renderView1, True)

# change representation type
fbm_1hdf5_6Display.SetRepresentationType('Volume')

# current camera placement for renderView1
renderView1.CameraPosition = [270.70218673844255, 348.0288767257049, 301.60357944779304]
renderView1.CameraFocalPoint = [63.5, 63.5, 63.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 109.9852262806237

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/fbb/single/h075/fbb_single_128_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
fbm_1hdf5_7 = NetCDFReader(FileName=['/scratch/snx3000/klye/fbm/single/H0_75/N64/fbm_1.hdf5'])
fbm_1hdf5_7.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(fbm_1hdf5_6, renderView1)

# show data in view
fbm_1hdf5_7Display = Show(fbm_1hdf5_7, renderView1)

# trace defaults for the display properties.
fbm_1hdf5_7Display.Representation = 'Outline'
fbm_1hdf5_7Display.ColorArrayName = [None, '']
fbm_1hdf5_7Display.OSPRayScaleArray = 'sample_0_E'
fbm_1hdf5_7Display.OSPRayScaleFunction = 'PiecewiseFunction'
fbm_1hdf5_7Display.SelectOrientationVectors = 'None'
fbm_1hdf5_7Display.ScaleFactor = 6.300000000000001
fbm_1hdf5_7Display.SelectScaleArray = 'None'
fbm_1hdf5_7Display.GlyphType = 'Arrow'
fbm_1hdf5_7Display.GlyphTableIndexArray = 'None'
fbm_1hdf5_7Display.GaussianRadius = 0.315
fbm_1hdf5_7Display.SetScaleArray = ['POINTS', 'sample_0_E']
fbm_1hdf5_7Display.ScaleTransferFunction = 'PiecewiseFunction'
fbm_1hdf5_7Display.OpacityArray = ['POINTS', 'sample_0_E']
fbm_1hdf5_7Display.OpacityTransferFunction = 'PiecewiseFunction'
fbm_1hdf5_7Display.DataAxesGrid = 'GridAxesRepresentation'
fbm_1hdf5_7Display.SelectionCellLabelFontFile = ''
fbm_1hdf5_7Display.SelectionPointLabelFontFile = ''
fbm_1hdf5_7Display.PolarAxes = 'PolarAxesRepresentation'
fbm_1hdf5_7Display.ScalarOpacityUnitDistance = 1.7320508075688774
fbm_1hdf5_7Display.Slice = 31

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
fbm_1hdf5_7Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_7Display.DataAxesGrid.XTitleFontFile = ''
fbm_1hdf5_7Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_7Display.DataAxesGrid.YTitleFontFile = ''
fbm_1hdf5_7Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_7Display.DataAxesGrid.ZTitleFontFile = ''
fbm_1hdf5_7Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_7Display.DataAxesGrid.XLabelFontFile = ''
fbm_1hdf5_7Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_7Display.DataAxesGrid.YLabelFontFile = ''
fbm_1hdf5_7Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_7Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
fbm_1hdf5_7Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_7Display.PolarAxes.PolarAxisTitleFontFile = ''
fbm_1hdf5_7Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_7Display.PolarAxes.PolarAxisLabelFontFile = ''
fbm_1hdf5_7Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_7Display.PolarAxes.LastRadialAxisTextFontFile = ''
fbm_1hdf5_7Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_7Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(fbm_1hdf5_7Display, ('POINTS', 'sample_0_rho'))

# rescale color and/or opacity maps used to include current data range
fbm_1hdf5_7Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
fbm_1hdf5_7Display.SetScalarBarVisibility(renderView1, True)

# change representation type
fbm_1hdf5_7Display.SetRepresentationType('Volume')

# current camera placement for renderView1
renderView1.CameraPosition = [134.28533672851876, 172.6442459347985, 149.61437405677924]
renderView1.CameraFocalPoint = [31.5, 31.5, 31.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 54.559600438419636

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/fbb/single/h075/fbb_single_64_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# hide data in view
Hide(fbm_1hdf5_7, renderView1)

# create a new 'NetCDF Reader'
fbm_1hdf5_8 = NetCDFReader(FileName=['/scratch/snx3000/klye/fbm/single/H0_5/N512/fbm_1.hdf5'])
fbm_1hdf5_8.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# show data in view
fbm_1hdf5_8Display = Show(fbm_1hdf5_8, renderView1)

# trace defaults for the display properties.
fbm_1hdf5_8Display.Representation = 'Outline'
fbm_1hdf5_8Display.ColorArrayName = [None, '']
fbm_1hdf5_8Display.OSPRayScaleArray = 'sample_0_E'
fbm_1hdf5_8Display.OSPRayScaleFunction = 'PiecewiseFunction'
fbm_1hdf5_8Display.SelectOrientationVectors = 'None'
fbm_1hdf5_8Display.ScaleFactor = 51.1
fbm_1hdf5_8Display.SelectScaleArray = 'None'
fbm_1hdf5_8Display.GlyphType = 'Arrow'
fbm_1hdf5_8Display.GlyphTableIndexArray = 'None'
fbm_1hdf5_8Display.GaussianRadius = 2.555
fbm_1hdf5_8Display.SetScaleArray = ['POINTS', 'sample_0_E']
fbm_1hdf5_8Display.ScaleTransferFunction = 'PiecewiseFunction'
fbm_1hdf5_8Display.OpacityArray = ['POINTS', 'sample_0_E']
fbm_1hdf5_8Display.OpacityTransferFunction = 'PiecewiseFunction'
fbm_1hdf5_8Display.DataAxesGrid = 'GridAxesRepresentation'
fbm_1hdf5_8Display.SelectionCellLabelFontFile = ''
fbm_1hdf5_8Display.SelectionPointLabelFontFile = ''
fbm_1hdf5_8Display.PolarAxes = 'PolarAxesRepresentation'
fbm_1hdf5_8Display.ScalarOpacityUnitDistance = 1.732050807568877
fbm_1hdf5_8Display.Slice = 255

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
fbm_1hdf5_8Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_8Display.DataAxesGrid.XTitleFontFile = ''
fbm_1hdf5_8Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_8Display.DataAxesGrid.YTitleFontFile = ''
fbm_1hdf5_8Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_8Display.DataAxesGrid.ZTitleFontFile = ''
fbm_1hdf5_8Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_8Display.DataAxesGrid.XLabelFontFile = ''
fbm_1hdf5_8Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_8Display.DataAxesGrid.YLabelFontFile = ''
fbm_1hdf5_8Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_8Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
fbm_1hdf5_8Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_8Display.PolarAxes.PolarAxisTitleFontFile = ''
fbm_1hdf5_8Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_8Display.PolarAxes.PolarAxisLabelFontFile = ''
fbm_1hdf5_8Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_8Display.PolarAxes.LastRadialAxisTextFontFile = ''
fbm_1hdf5_8Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_8Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(fbm_1hdf5)

# destroy fbm_1hdf5
Delete(fbm_1hdf5)
del fbm_1hdf5

# set active source
SetActiveSource(fbm_1hdf5_1)

# destroy fbm_1hdf5_1
Delete(fbm_1hdf5_1)
del fbm_1hdf5_1

# set active source
SetActiveSource(fbm_1hdf5_2)

# destroy fbm_1hdf5_2
Delete(fbm_1hdf5_2)
del fbm_1hdf5_2

# set active source
SetActiveSource(fbm_1hdf5_3)

# destroy fbm_1hdf5_3
Delete(fbm_1hdf5_3)
del fbm_1hdf5_3

# set active source
SetActiveSource(fbm_1hdf5_4)

# destroy fbm_1hdf5_4
Delete(fbm_1hdf5_4)
del fbm_1hdf5_4

# set active source
SetActiveSource(fbm_1hdf5_5)

# destroy fbm_1hdf5_5
Delete(fbm_1hdf5_5)
del fbm_1hdf5_5

# set active source
SetActiveSource(fbm_1hdf5_6)

# destroy fbm_1hdf5_6
Delete(fbm_1hdf5_6)
del fbm_1hdf5_6

# set active source
SetActiveSource(fbm_1hdf5_7)

# destroy fbm_1hdf5_7
Delete(fbm_1hdf5_7)
del fbm_1hdf5_7

# set active source
SetActiveSource(fbm_1hdf5_8)

# set scalar coloring
ColorBy(fbm_1hdf5_8Display, ('POINTS', 'sample_0_rho'))

# rescale color and/or opacity maps used to include current data range
fbm_1hdf5_8Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
fbm_1hdf5_8Display.SetScalarBarVisibility(renderView1, True)

# change representation type
fbm_1hdf5_8Display.SetRepresentationType('Volume')

# rescale color and/or opacity maps used to exactly fit the current data range
fbm_1hdf5_8Display.RescaleTransferFunctionToDataRange(False, True)

# rescale color and/or opacity maps used to exactly fit the current data range
fbm_1hdf5_8Display.RescaleTransferFunctionToDataRange(False, True)

# Rescale transfer function
sample_0_rhoLUT.RescaleTransferFunction(1.5, 5.0)

# Rescale transfer function
sample_0_rhoPWF.RescaleTransferFunction(1.5, 5.0)

# Rescale transfer function
sample_0_rhoLUT.RescaleTransferFunction(1.5, 6.0)

# Rescale transfer function
sample_0_rhoPWF.RescaleTransferFunction(1.5, 6.0)

# current camera placement for renderView1
renderView1.CameraPosition = [1089.2032867979854, 1400.3366614711433, 1213.538811793876]
renderView1.CameraFocalPoint = [255.5, 255.5, 255.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 442.53898133384814

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/fbb/single/h05/fbb_single_512_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
fbm_1hdf5 = NetCDFReader(FileName=['/scratch/snx3000/klye/fbm/single/H0_5/N256/fbm_1.hdf5'])
fbm_1hdf5.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(fbm_1hdf5_8, renderView1)

# show data in view
fbm_1hdf5Display = Show(fbm_1hdf5, renderView1)

# trace defaults for the display properties.
fbm_1hdf5Display.Representation = 'Outline'
fbm_1hdf5Display.ColorArrayName = [None, '']
fbm_1hdf5Display.OSPRayScaleArray = 'sample_0_E'
fbm_1hdf5Display.OSPRayScaleFunction = 'PiecewiseFunction'
fbm_1hdf5Display.SelectOrientationVectors = 'None'
fbm_1hdf5Display.ScaleFactor = 25.5
fbm_1hdf5Display.SelectScaleArray = 'None'
fbm_1hdf5Display.GlyphType = 'Arrow'
fbm_1hdf5Display.GlyphTableIndexArray = 'None'
fbm_1hdf5Display.GaussianRadius = 1.2750000000000001
fbm_1hdf5Display.SetScaleArray = ['POINTS', 'sample_0_E']
fbm_1hdf5Display.ScaleTransferFunction = 'PiecewiseFunction'
fbm_1hdf5Display.OpacityArray = ['POINTS', 'sample_0_E']
fbm_1hdf5Display.OpacityTransferFunction = 'PiecewiseFunction'
fbm_1hdf5Display.DataAxesGrid = 'GridAxesRepresentation'
fbm_1hdf5Display.SelectionCellLabelFontFile = ''
fbm_1hdf5Display.SelectionPointLabelFontFile = ''
fbm_1hdf5Display.PolarAxes = 'PolarAxesRepresentation'
fbm_1hdf5Display.ScalarOpacityUnitDistance = 1.7320508075688774
fbm_1hdf5Display.Slice = 127

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
fbm_1hdf5Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5Display.DataAxesGrid.XTitleFontFile = ''
fbm_1hdf5Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5Display.DataAxesGrid.YTitleFontFile = ''
fbm_1hdf5Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5Display.DataAxesGrid.ZTitleFontFile = ''
fbm_1hdf5Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5Display.DataAxesGrid.XLabelFontFile = ''
fbm_1hdf5Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5Display.DataAxesGrid.YLabelFontFile = ''
fbm_1hdf5Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
fbm_1hdf5Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5Display.PolarAxes.PolarAxisTitleFontFile = ''
fbm_1hdf5Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5Display.PolarAxes.PolarAxisLabelFontFile = ''
fbm_1hdf5Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5Display.PolarAxes.LastRadialAxisTextFontFile = ''
fbm_1hdf5Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(fbm_1hdf5Display, ('POINTS', 'sample_0_rho'))

# rescale color and/or opacity maps used to include current data range
fbm_1hdf5Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
fbm_1hdf5Display.SetScalarBarVisibility(renderView1, True)

# change representation type
fbm_1hdf5Display.SetRepresentationType('Volume')

# Rescale transfer function
sample_0_rhoLUT.RescaleTransferFunction(1.5, 6.0)

# Rescale transfer function
sample_0_rhoPWF.RescaleTransferFunction(1.5, 6.0)

# current camera placement for renderView1
renderView1.CameraPosition = [543.5358867582902, 698.7981383075178, 605.5819902298207]
renderView1.CameraFocalPoint = [127.5, 127.5, 127.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 220.83647796503186

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/fbb/single/h05/fbb_single_256_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# hide data in view
Hide(fbm_1hdf5, renderView1)

# create a new 'NetCDF Reader'
fbm_1hdf5_1 = NetCDFReader(FileName=['/scratch/snx3000/klye/fbm/single/H0_5/N128/fbm_1.hdf5'])
fbm_1hdf5_1.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# show data in view
fbm_1hdf5_1Display = Show(fbm_1hdf5_1, renderView1)

# trace defaults for the display properties.
fbm_1hdf5_1Display.Representation = 'Outline'
fbm_1hdf5_1Display.ColorArrayName = [None, '']
fbm_1hdf5_1Display.OSPRayScaleArray = 'sample_0_E'
fbm_1hdf5_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
fbm_1hdf5_1Display.SelectOrientationVectors = 'None'
fbm_1hdf5_1Display.ScaleFactor = 12.700000000000001
fbm_1hdf5_1Display.SelectScaleArray = 'None'
fbm_1hdf5_1Display.GlyphType = 'Arrow'
fbm_1hdf5_1Display.GlyphTableIndexArray = 'None'
fbm_1hdf5_1Display.GaussianRadius = 0.635
fbm_1hdf5_1Display.SetScaleArray = ['POINTS', 'sample_0_E']
fbm_1hdf5_1Display.ScaleTransferFunction = 'PiecewiseFunction'
fbm_1hdf5_1Display.OpacityArray = ['POINTS', 'sample_0_E']
fbm_1hdf5_1Display.OpacityTransferFunction = 'PiecewiseFunction'
fbm_1hdf5_1Display.DataAxesGrid = 'GridAxesRepresentation'
fbm_1hdf5_1Display.SelectionCellLabelFontFile = ''
fbm_1hdf5_1Display.SelectionPointLabelFontFile = ''
fbm_1hdf5_1Display.PolarAxes = 'PolarAxesRepresentation'
fbm_1hdf5_1Display.ScalarOpacityUnitDistance = 1.732050807568877
fbm_1hdf5_1Display.Slice = 63

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
fbm_1hdf5_1Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_1Display.DataAxesGrid.XTitleFontFile = ''
fbm_1hdf5_1Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_1Display.DataAxesGrid.YTitleFontFile = ''
fbm_1hdf5_1Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_1Display.DataAxesGrid.ZTitleFontFile = ''
fbm_1hdf5_1Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_1Display.DataAxesGrid.XLabelFontFile = ''
fbm_1hdf5_1Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_1Display.DataAxesGrid.YLabelFontFile = ''
fbm_1hdf5_1Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
fbm_1hdf5_1Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_1Display.PolarAxes.PolarAxisTitleFontFile = ''
fbm_1hdf5_1Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_1Display.PolarAxes.PolarAxisLabelFontFile = ''
fbm_1hdf5_1Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_1Display.PolarAxes.LastRadialAxisTextFontFile = ''
fbm_1hdf5_1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(fbm_1hdf5_1Display, ('POINTS', 'sample_0_rho'))

# rescale color and/or opacity maps used to include current data range
fbm_1hdf5_1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
fbm_1hdf5_1Display.SetScalarBarVisibility(renderView1, True)

# change representation type
fbm_1hdf5_1Display.SetRepresentationType('Volume')

# Rescale transfer function
sample_0_rhoLUT.RescaleTransferFunction(1.5, 6.0)

# Rescale transfer function
sample_0_rhoPWF.RescaleTransferFunction(1.5, 6.0)

# current camera placement for renderView1
renderView1.CameraPosition = [270.70218673844255, 348.0288767257049, 301.60357944779304]
renderView1.CameraFocalPoint = [63.5, 63.5, 63.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 109.9852262806237

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/fbb/single/h05/fbb_single_128_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
fbm_1hdf5_2 = NetCDFReader(FileName=['/scratch/snx3000/klye/fbm/single/H0_5/N64/fbm_1.hdf5'])
fbm_1hdf5_2.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(fbm_1hdf5_1, renderView1)

# show data in view
fbm_1hdf5_2Display = Show(fbm_1hdf5_2, renderView1)

# trace defaults for the display properties.
fbm_1hdf5_2Display.Representation = 'Outline'
fbm_1hdf5_2Display.ColorArrayName = [None, '']
fbm_1hdf5_2Display.OSPRayScaleArray = 'sample_0_E'
fbm_1hdf5_2Display.OSPRayScaleFunction = 'PiecewiseFunction'
fbm_1hdf5_2Display.SelectOrientationVectors = 'None'
fbm_1hdf5_2Display.ScaleFactor = 6.300000000000001
fbm_1hdf5_2Display.SelectScaleArray = 'None'
fbm_1hdf5_2Display.GlyphType = 'Arrow'
fbm_1hdf5_2Display.GlyphTableIndexArray = 'None'
fbm_1hdf5_2Display.GaussianRadius = 0.315
fbm_1hdf5_2Display.SetScaleArray = ['POINTS', 'sample_0_E']
fbm_1hdf5_2Display.ScaleTransferFunction = 'PiecewiseFunction'
fbm_1hdf5_2Display.OpacityArray = ['POINTS', 'sample_0_E']
fbm_1hdf5_2Display.OpacityTransferFunction = 'PiecewiseFunction'
fbm_1hdf5_2Display.DataAxesGrid = 'GridAxesRepresentation'
fbm_1hdf5_2Display.SelectionCellLabelFontFile = ''
fbm_1hdf5_2Display.SelectionPointLabelFontFile = ''
fbm_1hdf5_2Display.PolarAxes = 'PolarAxesRepresentation'
fbm_1hdf5_2Display.ScalarOpacityUnitDistance = 1.7320508075688774
fbm_1hdf5_2Display.Slice = 31

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
fbm_1hdf5_2Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_2Display.DataAxesGrid.XTitleFontFile = ''
fbm_1hdf5_2Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_2Display.DataAxesGrid.YTitleFontFile = ''
fbm_1hdf5_2Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_2Display.DataAxesGrid.ZTitleFontFile = ''
fbm_1hdf5_2Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_2Display.DataAxesGrid.XLabelFontFile = ''
fbm_1hdf5_2Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_2Display.DataAxesGrid.YLabelFontFile = ''
fbm_1hdf5_2Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_2Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
fbm_1hdf5_2Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_2Display.PolarAxes.PolarAxisTitleFontFile = ''
fbm_1hdf5_2Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_2Display.PolarAxes.PolarAxisLabelFontFile = ''
fbm_1hdf5_2Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_2Display.PolarAxes.LastRadialAxisTextFontFile = ''
fbm_1hdf5_2Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1hdf5_2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(fbm_1hdf5_2Display, ('POINTS', 'sample_0_rho'))

# rescale color and/or opacity maps used to include current data range
fbm_1hdf5_2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
fbm_1hdf5_2Display.SetScalarBarVisibility(renderView1, True)

# change representation type
fbm_1hdf5_2Display.SetRepresentationType('Volume')

# Rescale transfer function
sample_0_rhoLUT.RescaleTransferFunction(1.5, 6.0)

# Rescale transfer function
sample_0_rhoPWF.RescaleTransferFunction(1.5, 6.0)

# current camera placement for renderView1
renderView1.CameraPosition = [134.28533672851876, 172.6442459347985, 149.61437405677924]
renderView1.CameraFocalPoint = [31.5, 31.5, 31.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 54.559600438419636

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/fbb/single/h05/fbb_single_64_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# hide data in view
Hide(fbm_1hdf5_2, renderView1)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [134.28533672851876, 172.6442459347985, 149.61437405677924]
renderView1.CameraFocalPoint = [31.5, 31.5, 31.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 54.559600438419636

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).