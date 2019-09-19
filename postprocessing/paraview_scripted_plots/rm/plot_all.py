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
renderView1.ViewSize = [1612, 799]
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
richtmeyermeshkov_samples_mean_0hdf5 = NetCDFReader(FileName=['/scratch/snx3000/klye/richtmeyermeshkovstats/p0_05/N512/richtmeyermeshkov_samples_mean_0.hdf5'])
richtmeyermeshkov_samples_mean_0hdf5.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# show data in view
richtmeyermeshkov_samples_mean_0hdf5Display = Show(richtmeyermeshkov_samples_mean_0hdf5, renderView1)

# trace defaults for the display properties.
richtmeyermeshkov_samples_mean_0hdf5Display.Representation = 'Outline'
richtmeyermeshkov_samples_mean_0hdf5Display.ColorArrayName = [None, '']
richtmeyermeshkov_samples_mean_0hdf5Display.OSPRayScaleArray = 'E'
richtmeyermeshkov_samples_mean_0hdf5Display.OSPRayScaleFunction = 'PiecewiseFunction'
richtmeyermeshkov_samples_mean_0hdf5Display.SelectOrientationVectors = 'E'
richtmeyermeshkov_samples_mean_0hdf5Display.ScaleFactor = 51.1
richtmeyermeshkov_samples_mean_0hdf5Display.SelectScaleArray = 'E'
richtmeyermeshkov_samples_mean_0hdf5Display.GlyphType = 'Arrow'
richtmeyermeshkov_samples_mean_0hdf5Display.GlyphTableIndexArray = 'E'
richtmeyermeshkov_samples_mean_0hdf5Display.GaussianRadius = 2.555
richtmeyermeshkov_samples_mean_0hdf5Display.SetScaleArray = ['POINTS', 'E']
richtmeyermeshkov_samples_mean_0hdf5Display.ScaleTransferFunction = 'PiecewiseFunction'
richtmeyermeshkov_samples_mean_0hdf5Display.OpacityArray = ['POINTS', 'E']
richtmeyermeshkov_samples_mean_0hdf5Display.OpacityTransferFunction = 'PiecewiseFunction'
richtmeyermeshkov_samples_mean_0hdf5Display.DataAxesGrid = 'GridAxesRepresentation'
richtmeyermeshkov_samples_mean_0hdf5Display.SelectionCellLabelFontFile = ''
richtmeyermeshkov_samples_mean_0hdf5Display.SelectionPointLabelFontFile = ''
richtmeyermeshkov_samples_mean_0hdf5Display.PolarAxes = 'PolarAxesRepresentation'
richtmeyermeshkov_samples_mean_0hdf5Display.ScalarOpacityUnitDistance = 1.732050807568877
richtmeyermeshkov_samples_mean_0hdf5Display.Slice = 255

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
richtmeyermeshkov_samples_mean_0hdf5Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_mean_0hdf5Display.DataAxesGrid.XTitleFontFile = ''
richtmeyermeshkov_samples_mean_0hdf5Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_mean_0hdf5Display.DataAxesGrid.YTitleFontFile = ''
richtmeyermeshkov_samples_mean_0hdf5Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_mean_0hdf5Display.DataAxesGrid.ZTitleFontFile = ''
richtmeyermeshkov_samples_mean_0hdf5Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_mean_0hdf5Display.DataAxesGrid.XLabelFontFile = ''
richtmeyermeshkov_samples_mean_0hdf5Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_mean_0hdf5Display.DataAxesGrid.YLabelFontFile = ''
richtmeyermeshkov_samples_mean_0hdf5Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_mean_0hdf5Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
richtmeyermeshkov_samples_mean_0hdf5Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_mean_0hdf5Display.PolarAxes.PolarAxisTitleFontFile = ''
richtmeyermeshkov_samples_mean_0hdf5Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_mean_0hdf5Display.PolarAxes.PolarAxisLabelFontFile = ''
richtmeyermeshkov_samples_mean_0hdf5Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_mean_0hdf5Display.PolarAxes.LastRadialAxisTextFontFile = ''
richtmeyermeshkov_samples_mean_0hdf5Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_mean_0hdf5Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(richtmeyermeshkov_samples_mean_0hdf5Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
richtmeyermeshkov_samples_mean_0hdf5Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
richtmeyermeshkov_samples_mean_0hdf5Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'rho'
rhoLUT = GetColorTransferFunction('rho')
rhoLUT.RGBPoints = [0.7187113761901855, 0.231373, 0.298039, 0.752941, 1.3540561199188232, 0.865003, 0.865003, 0.865003, 1.989400863647461, 0.705882, 0.0156863, 0.14902]
rhoLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'rho'
rhoPWF = GetOpacityTransferFunction('rho')
rhoPWF.Points = [0.7187113761901855, 0.0, 0.5, 0.0, 1.989400863647461, 1.0, 0.5, 0.0]
rhoPWF.ScalarRangeInitialized = 1

# change representation type
richtmeyermeshkov_samples_mean_0hdf5Display.SetRepresentationType('Volume')

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
rhoLUT.ApplyPreset('Viridis (matplotlib)', True)

# Rescale transfer function
rhoLUT.RescaleTransferFunction(0.0, 1.98940086365)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(0.0, 1.98940086365)

# Rescale transfer function
rhoLUT.RescaleTransferFunction(0.8, 1.98940086365)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(0.8, 1.98940086365)

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.076778769493103, 0.22058823704719543, 0.5, 0.0, 1.989400863647461, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.076778769493103, 0.2132352888584137, 0.5, 0.0, 1.989400863647461, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.076778769493103, 0.19117647409439087, 0.5, 0.0, 1.989400863647461, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.0655580759048462, 0.04411764815449715, 0.5, 0.0, 1.989400863647461, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.0655580759048462, 0.036764707416296005, 0.5, 0.0, 1.989400863647461, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.0730385780334473, 0.0, 0.5, 0.0, 1.989400863647461, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.069298267364502, 0.0, 0.5, 0.0, 1.989400863647461, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.069298267364502, 0.014705882407724857, 0.5, 0.0, 1.989400863647461, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.069298267364502, 0.022058824077248573, 0.5, 0.0, 1.989400863647461, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.0730385780334473, 0.022058824077248573, 0.5, 0.0, 1.989400863647461, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.076778769493103, 0.05147058889269829, 0.5, 0.0, 1.989400863647461, 1.0, 0.5, 0.0]

# current camera placement for renderView1
renderView1.CameraPosition = [884.3686509629604, 1213.3783842724602, 1524.5719985679252]
renderView1.CameraFocalPoint = [255.5, 255.5, 255.49999999999997]
renderView1.CameraViewUp = [-0.12830694614311933, 0.8211007381558844, -0.556175246996204]
renderView1.CameraParallelScale = 442.53898133384814

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/rm/stats/rm_mean_512_eps_005_cm_0_0.png', renderView1, ImageResolution=[1216, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
richtmeyermeshkov_samples_mean_0hdf5_1 = NetCDFReader(FileName=['/scratch/snx3000/klye/richtmeyermeshkovstats/p0_05/N256/richtmeyermeshkov_samples_mean_0.hdf5'])
richtmeyermeshkov_samples_mean_0hdf5_1.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(richtmeyermeshkov_samples_mean_0hdf5, renderView1)

# show data in view
richtmeyermeshkov_samples_mean_0hdf5_1Display = Show(richtmeyermeshkov_samples_mean_0hdf5_1, renderView1)

# trace defaults for the display properties.
richtmeyermeshkov_samples_mean_0hdf5_1Display.Representation = 'Outline'
richtmeyermeshkov_samples_mean_0hdf5_1Display.ColorArrayName = [None, '']
richtmeyermeshkov_samples_mean_0hdf5_1Display.OSPRayScaleArray = 'E'
richtmeyermeshkov_samples_mean_0hdf5_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
richtmeyermeshkov_samples_mean_0hdf5_1Display.SelectOrientationVectors = 'E'
richtmeyermeshkov_samples_mean_0hdf5_1Display.ScaleFactor = 25.5
richtmeyermeshkov_samples_mean_0hdf5_1Display.SelectScaleArray = 'E'
richtmeyermeshkov_samples_mean_0hdf5_1Display.GlyphType = 'Arrow'
richtmeyermeshkov_samples_mean_0hdf5_1Display.GlyphTableIndexArray = 'E'
richtmeyermeshkov_samples_mean_0hdf5_1Display.GaussianRadius = 1.2750000000000001
richtmeyermeshkov_samples_mean_0hdf5_1Display.SetScaleArray = ['POINTS', 'E']
richtmeyermeshkov_samples_mean_0hdf5_1Display.ScaleTransferFunction = 'PiecewiseFunction'
richtmeyermeshkov_samples_mean_0hdf5_1Display.OpacityArray = ['POINTS', 'E']
richtmeyermeshkov_samples_mean_0hdf5_1Display.OpacityTransferFunction = 'PiecewiseFunction'
richtmeyermeshkov_samples_mean_0hdf5_1Display.DataAxesGrid = 'GridAxesRepresentation'
richtmeyermeshkov_samples_mean_0hdf5_1Display.SelectionCellLabelFontFile = ''
richtmeyermeshkov_samples_mean_0hdf5_1Display.SelectionPointLabelFontFile = ''
richtmeyermeshkov_samples_mean_0hdf5_1Display.PolarAxes = 'PolarAxesRepresentation'
richtmeyermeshkov_samples_mean_0hdf5_1Display.ScalarOpacityUnitDistance = 1.7320508075688774
richtmeyermeshkov_samples_mean_0hdf5_1Display.Slice = 127

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
richtmeyermeshkov_samples_mean_0hdf5_1Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_mean_0hdf5_1Display.DataAxesGrid.XTitleFontFile = ''
richtmeyermeshkov_samples_mean_0hdf5_1Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_mean_0hdf5_1Display.DataAxesGrid.YTitleFontFile = ''
richtmeyermeshkov_samples_mean_0hdf5_1Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_mean_0hdf5_1Display.DataAxesGrid.ZTitleFontFile = ''
richtmeyermeshkov_samples_mean_0hdf5_1Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_mean_0hdf5_1Display.DataAxesGrid.XLabelFontFile = ''
richtmeyermeshkov_samples_mean_0hdf5_1Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_mean_0hdf5_1Display.DataAxesGrid.YLabelFontFile = ''
richtmeyermeshkov_samples_mean_0hdf5_1Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_mean_0hdf5_1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
richtmeyermeshkov_samples_mean_0hdf5_1Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_mean_0hdf5_1Display.PolarAxes.PolarAxisTitleFontFile = ''
richtmeyermeshkov_samples_mean_0hdf5_1Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_mean_0hdf5_1Display.PolarAxes.PolarAxisLabelFontFile = ''
richtmeyermeshkov_samples_mean_0hdf5_1Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_mean_0hdf5_1Display.PolarAxes.LastRadialAxisTextFontFile = ''
richtmeyermeshkov_samples_mean_0hdf5_1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_mean_0hdf5_1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(richtmeyermeshkov_samples_mean_0hdf5_1Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
richtmeyermeshkov_samples_mean_0hdf5_1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
richtmeyermeshkov_samples_mean_0hdf5_1Display.SetScalarBarVisibility(renderView1, True)

# change representation type
richtmeyermeshkov_samples_mean_0hdf5_1Display.SetRepresentationType('Volume')

# current camera placement for renderView1
renderView1.CameraPosition = [441.3189941204596, 605.501933443204, 760.7942458607062]
renderView1.CameraFocalPoint = [127.5, 127.5, 127.5]
renderView1.CameraViewUp = [-0.12830694614311933, 0.8211007381558844, -0.556175246996204]
renderView1.CameraParallelScale = 220.83647796503186

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/rm/stats/rm_mean_256_eps_005_cm_0_0.png', renderView1, ImageResolution=[1216, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
richtmeyermeshkov_samples_mean_0hdf5_2 = NetCDFReader(FileName=['/scratch/snx3000/klye/richtmeyermeshkovstats/p0_05/N128/richtmeyermeshkov_samples_mean_0.hdf5'])
richtmeyermeshkov_samples_mean_0hdf5_2.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(richtmeyermeshkov_samples_mean_0hdf5_1, renderView1)

# show data in view
richtmeyermeshkov_samples_mean_0hdf5_2Display = Show(richtmeyermeshkov_samples_mean_0hdf5_2, renderView1)

# trace defaults for the display properties.
richtmeyermeshkov_samples_mean_0hdf5_2Display.Representation = 'Outline'
richtmeyermeshkov_samples_mean_0hdf5_2Display.ColorArrayName = [None, '']
richtmeyermeshkov_samples_mean_0hdf5_2Display.OSPRayScaleArray = 'E'
richtmeyermeshkov_samples_mean_0hdf5_2Display.OSPRayScaleFunction = 'PiecewiseFunction'
richtmeyermeshkov_samples_mean_0hdf5_2Display.SelectOrientationVectors = 'E'
richtmeyermeshkov_samples_mean_0hdf5_2Display.ScaleFactor = 12.700000000000001
richtmeyermeshkov_samples_mean_0hdf5_2Display.SelectScaleArray = 'E'
richtmeyermeshkov_samples_mean_0hdf5_2Display.GlyphType = 'Arrow'
richtmeyermeshkov_samples_mean_0hdf5_2Display.GlyphTableIndexArray = 'E'
richtmeyermeshkov_samples_mean_0hdf5_2Display.GaussianRadius = 0.635
richtmeyermeshkov_samples_mean_0hdf5_2Display.SetScaleArray = ['POINTS', 'E']
richtmeyermeshkov_samples_mean_0hdf5_2Display.ScaleTransferFunction = 'PiecewiseFunction'
richtmeyermeshkov_samples_mean_0hdf5_2Display.OpacityArray = ['POINTS', 'E']
richtmeyermeshkov_samples_mean_0hdf5_2Display.OpacityTransferFunction = 'PiecewiseFunction'
richtmeyermeshkov_samples_mean_0hdf5_2Display.DataAxesGrid = 'GridAxesRepresentation'
richtmeyermeshkov_samples_mean_0hdf5_2Display.SelectionCellLabelFontFile = ''
richtmeyermeshkov_samples_mean_0hdf5_2Display.SelectionPointLabelFontFile = ''
richtmeyermeshkov_samples_mean_0hdf5_2Display.PolarAxes = 'PolarAxesRepresentation'
richtmeyermeshkov_samples_mean_0hdf5_2Display.ScalarOpacityUnitDistance = 1.732050807568877
richtmeyermeshkov_samples_mean_0hdf5_2Display.Slice = 63

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
richtmeyermeshkov_samples_mean_0hdf5_2Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_mean_0hdf5_2Display.DataAxesGrid.XTitleFontFile = ''
richtmeyermeshkov_samples_mean_0hdf5_2Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_mean_0hdf5_2Display.DataAxesGrid.YTitleFontFile = ''
richtmeyermeshkov_samples_mean_0hdf5_2Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_mean_0hdf5_2Display.DataAxesGrid.ZTitleFontFile = ''
richtmeyermeshkov_samples_mean_0hdf5_2Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_mean_0hdf5_2Display.DataAxesGrid.XLabelFontFile = ''
richtmeyermeshkov_samples_mean_0hdf5_2Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_mean_0hdf5_2Display.DataAxesGrid.YLabelFontFile = ''
richtmeyermeshkov_samples_mean_0hdf5_2Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_mean_0hdf5_2Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
richtmeyermeshkov_samples_mean_0hdf5_2Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_mean_0hdf5_2Display.PolarAxes.PolarAxisTitleFontFile = ''
richtmeyermeshkov_samples_mean_0hdf5_2Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_mean_0hdf5_2Display.PolarAxes.PolarAxisLabelFontFile = ''
richtmeyermeshkov_samples_mean_0hdf5_2Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_mean_0hdf5_2Display.PolarAxes.LastRadialAxisTextFontFile = ''
richtmeyermeshkov_samples_mean_0hdf5_2Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_mean_0hdf5_2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(richtmeyermeshkov_samples_mean_0hdf5_2Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
richtmeyermeshkov_samples_mean_0hdf5_2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
richtmeyermeshkov_samples_mean_0hdf5_2Display.SetScalarBarVisibility(renderView1, True)

# change representation type
richtmeyermeshkov_samples_mean_0hdf5_2Display.SetRepresentationType('Volume')

# current camera placement for renderView1
renderView1.CameraPosition = [219.7941656992093, 301.5637080285761, 378.9053695070968]
renderView1.CameraFocalPoint = [63.5, 63.5, 63.5]
renderView1.CameraViewUp = [-0.12830694614311933, 0.8211007381558844, -0.556175246996204]
renderView1.CameraParallelScale = 109.9852262806237

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/rm/stats/rm_mean_128_eps_005_cm_0_0.png', renderView1, ImageResolution=[1216, 799], 
    # PNG options
    CompressionLevel='0')

# hide data in view
Hide(richtmeyermeshkov_samples_mean_0hdf5_2, renderView1)

# create a new 'NetCDF Reader'
richtmeyermeshkov_samples_mean_0hdf5_3 = NetCDFReader(FileName=['/scratch/snx3000/klye/richtmeyermeshkovstats/p0_05/N64/richtmeyermeshkov_samples_mean_0.hdf5'])
richtmeyermeshkov_samples_mean_0hdf5_3.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# show data in view
richtmeyermeshkov_samples_mean_0hdf5_3Display = Show(richtmeyermeshkov_samples_mean_0hdf5_3, renderView1)

# trace defaults for the display properties.
richtmeyermeshkov_samples_mean_0hdf5_3Display.Representation = 'Outline'
richtmeyermeshkov_samples_mean_0hdf5_3Display.ColorArrayName = [None, '']
richtmeyermeshkov_samples_mean_0hdf5_3Display.OSPRayScaleArray = 'E'
richtmeyermeshkov_samples_mean_0hdf5_3Display.OSPRayScaleFunction = 'PiecewiseFunction'
richtmeyermeshkov_samples_mean_0hdf5_3Display.SelectOrientationVectors = 'E'
richtmeyermeshkov_samples_mean_0hdf5_3Display.ScaleFactor = 6.300000000000001
richtmeyermeshkov_samples_mean_0hdf5_3Display.SelectScaleArray = 'E'
richtmeyermeshkov_samples_mean_0hdf5_3Display.GlyphType = 'Arrow'
richtmeyermeshkov_samples_mean_0hdf5_3Display.GlyphTableIndexArray = 'E'
richtmeyermeshkov_samples_mean_0hdf5_3Display.GaussianRadius = 0.315
richtmeyermeshkov_samples_mean_0hdf5_3Display.SetScaleArray = ['POINTS', 'E']
richtmeyermeshkov_samples_mean_0hdf5_3Display.ScaleTransferFunction = 'PiecewiseFunction'
richtmeyermeshkov_samples_mean_0hdf5_3Display.OpacityArray = ['POINTS', 'E']
richtmeyermeshkov_samples_mean_0hdf5_3Display.OpacityTransferFunction = 'PiecewiseFunction'
richtmeyermeshkov_samples_mean_0hdf5_3Display.DataAxesGrid = 'GridAxesRepresentation'
richtmeyermeshkov_samples_mean_0hdf5_3Display.SelectionCellLabelFontFile = ''
richtmeyermeshkov_samples_mean_0hdf5_3Display.SelectionPointLabelFontFile = ''
richtmeyermeshkov_samples_mean_0hdf5_3Display.PolarAxes = 'PolarAxesRepresentation'
richtmeyermeshkov_samples_mean_0hdf5_3Display.ScalarOpacityUnitDistance = 1.7320508075688774
richtmeyermeshkov_samples_mean_0hdf5_3Display.Slice = 31

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
richtmeyermeshkov_samples_mean_0hdf5_3Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_mean_0hdf5_3Display.DataAxesGrid.XTitleFontFile = ''
richtmeyermeshkov_samples_mean_0hdf5_3Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_mean_0hdf5_3Display.DataAxesGrid.YTitleFontFile = ''
richtmeyermeshkov_samples_mean_0hdf5_3Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_mean_0hdf5_3Display.DataAxesGrid.ZTitleFontFile = ''
richtmeyermeshkov_samples_mean_0hdf5_3Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_mean_0hdf5_3Display.DataAxesGrid.XLabelFontFile = ''
richtmeyermeshkov_samples_mean_0hdf5_3Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_mean_0hdf5_3Display.DataAxesGrid.YLabelFontFile = ''
richtmeyermeshkov_samples_mean_0hdf5_3Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_mean_0hdf5_3Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
richtmeyermeshkov_samples_mean_0hdf5_3Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_mean_0hdf5_3Display.PolarAxes.PolarAxisTitleFontFile = ''
richtmeyermeshkov_samples_mean_0hdf5_3Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_mean_0hdf5_3Display.PolarAxes.PolarAxisLabelFontFile = ''
richtmeyermeshkov_samples_mean_0hdf5_3Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_mean_0hdf5_3Display.PolarAxes.LastRadialAxisTextFontFile = ''
richtmeyermeshkov_samples_mean_0hdf5_3Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_mean_0hdf5_3Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(richtmeyermeshkov_samples_mean_0hdf5_3Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
richtmeyermeshkov_samples_mean_0hdf5_3Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
richtmeyermeshkov_samples_mean_0hdf5_3Display.SetScalarBarVisibility(renderView1, True)

# change representation type
richtmeyermeshkov_samples_mean_0hdf5_3Display.SetRepresentationType('Volume')

# current camera placement for renderView1
renderView1.CameraPosition = [109.03175148858415, 149.5945953212622, 187.9609313302921]
renderView1.CameraFocalPoint = [31.5, 31.5, 31.5]
renderView1.CameraViewUp = [-0.12830694614311933, 0.8211007381558844, -0.556175246996204]
renderView1.CameraParallelScale = 54.559600438419636

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/rm/stats/rm_mean_64_eps_005_cm_0_0.png', renderView1, ImageResolution=[1216, 799])

# hide data in view
Hide(richtmeyermeshkov_samples_mean_0hdf5_3, renderView1)

# set active source
SetActiveSource(richtmeyermeshkov_samples_mean_0hdf5)

# set active source
SetActiveSource(richtmeyermeshkov_samples_mean_0hdf5)

# show data in view
richtmeyermeshkov_samples_mean_0hdf5Display = Show(richtmeyermeshkov_samples_mean_0hdf5, renderView1)

# show color bar/color legend
richtmeyermeshkov_samples_mean_0hdf5Display.SetScalarBarVisibility(renderView1, True)

# reset view to fit data
renderView1.ResetCamera()

# Rescale transfer function
rhoLUT.RescaleTransferFunction(0.8, 2.30617189407)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(0.8, 2.30617189407)

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.169438362121582, 0.029411764815449715, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.188383936882019, 0.036764707416296005, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.1978566646575928, 0.036764707416296005, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.2120659351348877, 0.05147058889269829, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.2310113906860352, 0.05882352963089943, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.2404842376708984, 0.06617647409439087, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.2499569654464722, 0.06617647409439087, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.2546933889389038, 0.06617647409439087, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.2594298124313354, 0.06617647409439087, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.2878481149673462, 0.08088235557079315, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.29732084274292, 0.08088235557079315, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.3399484157562256, 0.09558823704719543, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.3494211435317993, 0.09558823704719543, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.354157567024231, 0.09558823704719543, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.354157567024231, 0.10294117778539658, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.3683667182922363, 0.10294117778539658, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.396785020828247, 0.10294117778539658, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.396785020828247, 0.09558823704719543, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.4062578678131104, 0.0882352963089943, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.410994291305542, 0.0882352963089943, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.4204670190811157, 0.0882352963089943, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.4252034425735474, 0.0882352963089943, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.4299397468566895, 0.06617647409439087, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.4394125938415527, 0.05882352963089943, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.4441490173339844, 0.05147058889269829, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.4488853216171265, 0.036764707416296005, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.4441490173339844, 0.014705882407724857, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.4394125938415527, 0.014705882407724857, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.4299397468566895, 0.029411764815449715, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.4252034425735474, 0.036764707416296005, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.4015214443206787, 0.0882352963089943, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.4062578678131104, 0.0882352963089943, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.4252034425735474, 0.08088235557079315, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.4252034425735474, 0.07352941483259201, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.4252034425735474, 0.06617647409439087, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.4252034425735474, 0.05882352963089943, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.415730595588684, 0.05147058889269829, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.4062578678131104, 0.05147058889269829, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.4062578678131104, 0.04411764815449715, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.4062578678131104, 0.036764707416296005, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.4062578678131104, 0.029411764815449715, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.4062578678131104, 0.022058824077248573, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.4062578678131104, 0.014705882407724857, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.4062578678131104, 0.007352941203862429, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.4062578678131104, 0.0, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.4015214443206787, 0.014705882407724857, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.396785020828247, 0.05147058889269829, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.410994291305542, 0.05882352963089943, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.4062578678131104, 0.05882352963089943, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.3873122930526733, 0.13970588147640228, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.3873122930526733, 0.15441176295280457, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.3873122930526733, 0.1764705926179886, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.3873122930526733, 0.18382352590560913, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.3873122930526733, 0.19117647409439087, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.3873122930526733, 0.1985294073820114, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.3825758695602417, 0.20588235557079315, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.3825758695602417, 0.22058823704719543, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.3825758695602417, 0.22794117033481598, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.3778395652770996, 0.24264706671237946, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.373103141784668, 0.24264706671237946, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.373103141784668, 0.29411765933036804, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.3494211435317993, 0.3014705777168274, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 1.3446848392486572, 0.3014705777168274, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [0.8, 0.0, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# create a new 'Clip'
clip1 = Clip(Input=richtmeyermeshkov_samples_mean_0hdf5)
clip1.ClipType = 'Plane'
clip1.Scalars = ['POINTS', 'E']
clip1.Value = 3.2175498008728027

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [255.5, 255.5, 255.5]

# Properties modified on clip1.ClipType
clip1.ClipType.Normal = [0.9678693280821475, 0.24281461630956008, -0.06534543491517636]

# Properties modified on clip1.ClipType
clip1.ClipType.Normal = [0.9678693280821475, 0.24281461630956008, -0.06534543491517636]

# show data in view
clip1Display = Show(clip1, renderView1)

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.ColorArrayName = ['POINTS', 'rho']
clip1Display.LookupTable = rhoLUT
clip1Display.OSPRayScaleArray = 'E'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.SelectOrientationVectors = 'E'
clip1Display.ScaleFactor = 51.1
clip1Display.SelectScaleArray = 'E'
clip1Display.GlyphType = 'Arrow'
clip1Display.GlyphTableIndexArray = 'E'
clip1Display.GaussianRadius = 2.555
clip1Display.SetScaleArray = ['POINTS', 'E']
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityArray = ['POINTS', 'E']
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.SelectionCellLabelFontFile = ''
clip1Display.SelectionPointLabelFontFile = ''
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityFunction = rhoPWF
clip1Display.ScalarOpacityUnitDistance = 1.960434729785341

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
clip1Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
clip1Display.DataAxesGrid.XTitleFontFile = ''
clip1Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
clip1Display.DataAxesGrid.YTitleFontFile = ''
clip1Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
clip1Display.DataAxesGrid.ZTitleFontFile = ''
clip1Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
clip1Display.DataAxesGrid.XLabelFontFile = ''
clip1Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
clip1Display.DataAxesGrid.YLabelFontFile = ''
clip1Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
clip1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
clip1Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
clip1Display.PolarAxes.PolarAxisTitleFontFile = ''
clip1Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
clip1Display.PolarAxes.PolarAxisLabelFontFile = ''
clip1Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
clip1Display.PolarAxes.LastRadialAxisTextFontFile = ''
clip1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
clip1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# Rescale transfer function
rhoLUT.RescaleTransferFunction(0.71871137619, 2.30617189407)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(0.71871137619, 2.30617189407)

# Properties modified on clip1Display
clip1Display.Opacity = 0.0

# Properties modified on clip1Display
clip1Display.Opacity = 0.65

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=clip1.ClipType)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=clip1.ClipType)

# set active source
SetActiveSource(richtmeyermeshkov_samples_mean_0hdf5)

# hide data in view
Hide(clip1, renderView1)

# show data in view
richtmeyermeshkov_samples_mean_0hdf5Display = Show(richtmeyermeshkov_samples_mean_0hdf5, renderView1)

# show color bar/color legend
richtmeyermeshkov_samples_mean_0hdf5Display.SetScalarBarVisibility(renderView1, True)

# destroy clip1
Delete(clip1)
del clip1

# create a new 'Slice'
slice1 = Slice(Input=richtmeyermeshkov_samples_mean_0hdf5)
slice1.SliceType = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [255.5, 255.5, 255.5]

# set active source
SetActiveSource(richtmeyermeshkov_samples_mean_0hdf5)

# destroy slice1
Delete(slice1)
del slice1

# create a new 'Clip'
clip1 = Clip(Input=richtmeyermeshkov_samples_mean_0hdf5)
clip1.ClipType = 'Plane'
clip1.Scalars = ['POINTS', 'E']
clip1.Value = 3.2175498008728027

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [255.5, 255.5, 255.5]

# Properties modified on clip1.ClipType
clip1.ClipType.Origin = [227.2795950579668, 255.5, 255.5]
clip1.ClipType.Normal = [0.8086026617387926, -0.36957187659081414, -0.4577972951668498]

# Properties modified on clip1.ClipType
clip1.ClipType.Origin = [227.2795950579668, 255.5, 255.5]
clip1.ClipType.Normal = [0.8086026617387926, -0.36957187659081414, -0.4577972951668498]

# show data in view
clip1Display = Show(clip1, renderView1)

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.ColorArrayName = ['POINTS', 'rho']
clip1Display.LookupTable = rhoLUT
clip1Display.OSPRayScaleArray = 'E'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.SelectOrientationVectors = 'E'
clip1Display.ScaleFactor = 51.1
clip1Display.SelectScaleArray = 'E'
clip1Display.GlyphType = 'Arrow'
clip1Display.GlyphTableIndexArray = 'E'
clip1Display.GaussianRadius = 2.555
clip1Display.SetScaleArray = ['POINTS', 'E']
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityArray = ['POINTS', 'E']
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.SelectionCellLabelFontFile = ''
clip1Display.SelectionPointLabelFontFile = ''
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityFunction = rhoPWF
clip1Display.ScalarOpacityUnitDistance = 2.2058271804486402

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
clip1Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
clip1Display.DataAxesGrid.XTitleFontFile = ''
clip1Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
clip1Display.DataAxesGrid.YTitleFontFile = ''
clip1Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
clip1Display.DataAxesGrid.ZTitleFontFile = ''
clip1Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
clip1Display.DataAxesGrid.XLabelFontFile = ''
clip1Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
clip1Display.DataAxesGrid.YLabelFontFile = ''
clip1Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
clip1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
clip1Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
clip1Display.PolarAxes.PolarAxisTitleFontFile = ''
clip1Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
clip1Display.PolarAxes.PolarAxisLabelFontFile = ''
clip1Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
clip1Display.PolarAxes.LastRadialAxisTextFontFile = ''
clip1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
clip1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on clip1Display
clip1Display.Opacity = 0.48

# set active source
SetActiveSource(richtmeyermeshkov_samples_mean_0hdf5)

# hide data in view
Hide(clip1, renderView1)

# show data in view
richtmeyermeshkov_samples_mean_0hdf5Display = Show(richtmeyermeshkov_samples_mean_0hdf5, renderView1)

# show color bar/color legend
richtmeyermeshkov_samples_mean_0hdf5Display.SetScalarBarVisibility(renderView1, True)

# destroy clip1
Delete(clip1)
del clip1

# create a new 'Clip'
clip1 = Clip(Input=richtmeyermeshkov_samples_mean_0hdf5)
clip1.ClipType = 'Plane'
clip1.Scalars = ['POINTS', 'E']
clip1.Value = 3.2175498008728027

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [255.5, 255.5, 255.5]

# Properties modified on renderView1
renderView1.EnableOSPRay = 1

# show data in view
clip1Display = Show(clip1, renderView1)

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.ColorArrayName = ['POINTS', 'rho']
clip1Display.LookupTable = rhoLUT
clip1Display.OSPRayScaleArray = 'E'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.SelectOrientationVectors = 'E'
clip1Display.ScaleFactor = 51.1
clip1Display.SelectScaleArray = 'E'
clip1Display.GlyphType = 'Arrow'
clip1Display.GlyphTableIndexArray = 'E'
clip1Display.GaussianRadius = 2.555
clip1Display.SetScaleArray = ['POINTS', 'E']
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityArray = ['POINTS', 'E']
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.SelectionCellLabelFontFile = ''
clip1Display.SelectionPointLabelFontFile = ''
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityFunction = rhoPWF
clip1Display.ScalarOpacityUnitDistance = 1.8886503812854778

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
clip1Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
clip1Display.DataAxesGrid.XTitleFontFile = ''
clip1Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
clip1Display.DataAxesGrid.YTitleFontFile = ''
clip1Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
clip1Display.DataAxesGrid.ZTitleFontFile = ''
clip1Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
clip1Display.DataAxesGrid.XLabelFontFile = ''
clip1Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
clip1Display.DataAxesGrid.YLabelFontFile = ''
clip1Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
clip1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
clip1Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
clip1Display.PolarAxes.PolarAxisTitleFontFile = ''
clip1Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
clip1Display.PolarAxes.PolarAxisLabelFontFile = ''
clip1Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
clip1Display.PolarAxes.LastRadialAxisTextFontFile = ''
clip1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
clip1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(richtmeyermeshkov_samples_mean_0hdf5)

# hide data in view
Hide(clip1, renderView1)

# show data in view
richtmeyermeshkov_samples_mean_0hdf5Display = Show(richtmeyermeshkov_samples_mean_0hdf5, renderView1)

# show color bar/color legend
richtmeyermeshkov_samples_mean_0hdf5Display.SetScalarBarVisibility(renderView1, True)

# destroy clip1
Delete(clip1)
del clip1

# Rescale transfer function
rhoLUT.RescaleTransferFunction(1.0, 2.30617189407)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(1.0, 2.30617189407)

# Properties modified on rhoPWF
rhoPWF.Points = [1.0, 0.0, 0.5, 0.0, 1.2259101867675781, 0.1764705926179886, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [1.0, 0.0, 0.5, 0.0, 1.221802830696106, 0.16911764442920685, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [1.0, 0.0, 0.5, 0.0, 1.221802830696106, 0.1617647111415863, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [1.0, 0.0, 0.5, 0.0, 1.2300176620483398, 0.0882352963089943, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [1.0, 0.0, 0.5, 0.0, 1.2341251373291016, 0.08088235557079315, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [1.0, 0.0, 0.5, 0.0, 1.2341251373291016, 0.07352941483259201, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [1.0, 0.0, 0.5, 0.0, 1.2341251373291016, 0.06617647409439087, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [1.0, 0.0, 0.5, 0.0, 1.2341251373291016, 0.05882352963089943, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [1.0, 0.0, 0.5, 0.0, 1.2341251373291016, 0.05147058889269829, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [1.0, 0.0, 0.5, 0.0, 1.2341251373291016, 0.04411764815449715, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [1.0, 0.0, 0.5, 0.0, 1.2300176620483398, 0.04411764815449715, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [1.0, 0.0, 0.5, 0.0, 1.2300176620483398, 0.036764707416296005, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [1.0, 0.0, 0.5, 0.0, 1.2259101867675781, 0.029411764815449715, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [1.0, 0.0, 0.5, 0.0, 1.2259101867675781, 0.022058824077248573, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [1.0, 0.0, 0.5, 0.0, 1.2259101867675781, 0.029411764815449715, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [1.0, 0.0, 0.5, 0.0, 1.221802830696106, 0.029411764815449715, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [1.0, 0.0, 0.5, 0.0, 1.221802830696106, 0.036764707416296005, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [1.0, 0.0, 0.5, 0.0, 1.221802830696106, 0.029411764815449715, 0.5, 0.0, 2.3061718940734863, 1.0, 0.5, 0.0]

# current camera placement for renderView1
renderView1.CameraPosition = [-868.5819039717063, 1275.9312669828753, -531.0814765787152]
renderView1.CameraFocalPoint = [255.50000000000048, 255.49999999999926, 255.49999999999915]
renderView1.CameraViewUp = [-0.4383012310895304, -0.799467568808763, -0.4107841735612608]
renderView1.CameraParallelScale = 442.53898133384814

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/rm/stats/rm_mean_512_eps_005_cm_1_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# set active source
SetActiveSource(richtmeyermeshkov_samples_mean_0hdf5_1)

# hide data in view
Hide(richtmeyermeshkov_samples_mean_0hdf5, renderView1)

# set active source
SetActiveSource(richtmeyermeshkov_samples_mean_0hdf5_1)

# show data in view
richtmeyermeshkov_samples_mean_0hdf5_1Display = Show(richtmeyermeshkov_samples_mean_0hdf5_1, renderView1)

# show color bar/color legend
richtmeyermeshkov_samples_mean_0hdf5_1Display.SetScalarBarVisibility(renderView1, True)

# reset view to fit data
renderView1.ResetCamera()

# current camera placement for renderView1
renderView1.CameraPosition = [-433.44106753968697, 636.717168455242, -265.021089095046]
renderView1.CameraFocalPoint = [127.5, 127.5, 127.5]
renderView1.CameraViewUp = [-0.4383012310895304, -0.799467568808763, -0.4107841735612608]
renderView1.CameraParallelScale = 220.83647796503186

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/rm/stats/rm_mean_256_eps_005_cm_1_0.png', renderView1, ImageResolution=[1107, 799])

# hide data in view
Hide(richtmeyermeshkov_samples_mean_0hdf5_1, renderView1)

# set active source
SetActiveSource(richtmeyermeshkov_samples_mean_0hdf5_2)

# set active source
SetActiveSource(richtmeyermeshkov_samples_mean_0hdf5_2)

# show data in view
richtmeyermeshkov_samples_mean_0hdf5_2Display = Show(richtmeyermeshkov_samples_mean_0hdf5_2, renderView1)

# show color bar/color legend
richtmeyermeshkov_samples_mean_0hdf5_2Display.SetScalarBarVisibility(renderView1, True)

# reset view to fit data
renderView1.ResetCamera()

# current camera placement for renderView1
renderView1.CameraPosition = [-215.8706493236872, 317.11011919143425, -131.99089535321895]
renderView1.CameraFocalPoint = [63.5, 63.5, 63.5]
renderView1.CameraViewUp = [-0.4383012310895304, -0.799467568808763, -0.4107841735612608]
renderView1.CameraParallelScale = 109.9852262806237

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/rm/stats/rm_mean_128_eps_005_cm_1_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# set active source
SetActiveSource(richtmeyermeshkov_samples_mean_0hdf5_3)

# hide data in view
Hide(richtmeyermeshkov_samples_mean_0hdf5_2, renderView1)

# set active source
SetActiveSource(richtmeyermeshkov_samples_mean_0hdf5_3)

# show data in view
richtmeyermeshkov_samples_mean_0hdf5_3Display = Show(richtmeyermeshkov_samples_mean_0hdf5_3, renderView1)

# show color bar/color legend
richtmeyermeshkov_samples_mean_0hdf5_3Display.SetScalarBarVisibility(renderView1, True)

# reset view to fit data
renderView1.ResetCamera()

# current camera placement for renderView1
renderView1.CameraPosition = [-107.08544021568736, 157.30659455953037, -65.47579848230548]
renderView1.CameraFocalPoint = [31.5, 31.5, 31.5]
renderView1.CameraViewUp = [-0.4383012310895304, -0.799467568808763, -0.4107841735612608]
renderView1.CameraParallelScale = 54.559600438419636

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/rm/stats/rm_mean_64_eps_005_cm_1_0.png', renderView1, ImageResolution=[1107, 799])

# hide data in view
Hide(richtmeyermeshkov_samples_mean_0hdf5_3, renderView1)

# create a new 'NetCDF Reader'
richtmeyermeshkov_samples_variance_0hdf5 = NetCDFReader(FileName=['/scratch/snx3000/klye/richtmeyermeshkovstats/p0_05/N512/richtmeyermeshkov_samples_variance_0.hdf5'])
richtmeyermeshkov_samples_variance_0hdf5.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# show data in view
richtmeyermeshkov_samples_variance_0hdf5Display = Show(richtmeyermeshkov_samples_variance_0hdf5, renderView1)

# trace defaults for the display properties.
richtmeyermeshkov_samples_variance_0hdf5Display.Representation = 'Outline'
richtmeyermeshkov_samples_variance_0hdf5Display.ColorArrayName = [None, '']
richtmeyermeshkov_samples_variance_0hdf5Display.OSPRayScaleArray = 'E'
richtmeyermeshkov_samples_variance_0hdf5Display.OSPRayScaleFunction = 'PiecewiseFunction'
richtmeyermeshkov_samples_variance_0hdf5Display.SelectOrientationVectors = 'E'
richtmeyermeshkov_samples_variance_0hdf5Display.ScaleFactor = 51.1
richtmeyermeshkov_samples_variance_0hdf5Display.SelectScaleArray = 'E'
richtmeyermeshkov_samples_variance_0hdf5Display.GlyphType = 'Arrow'
richtmeyermeshkov_samples_variance_0hdf5Display.GlyphTableIndexArray = 'E'
richtmeyermeshkov_samples_variance_0hdf5Display.GaussianRadius = 2.555
richtmeyermeshkov_samples_variance_0hdf5Display.SetScaleArray = ['POINTS', 'E']
richtmeyermeshkov_samples_variance_0hdf5Display.ScaleTransferFunction = 'PiecewiseFunction'
richtmeyermeshkov_samples_variance_0hdf5Display.OpacityArray = ['POINTS', 'E']
richtmeyermeshkov_samples_variance_0hdf5Display.OpacityTransferFunction = 'PiecewiseFunction'
richtmeyermeshkov_samples_variance_0hdf5Display.DataAxesGrid = 'GridAxesRepresentation'
richtmeyermeshkov_samples_variance_0hdf5Display.SelectionCellLabelFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5Display.SelectionPointLabelFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5Display.PolarAxes = 'PolarAxesRepresentation'
richtmeyermeshkov_samples_variance_0hdf5Display.ScalarOpacityUnitDistance = 1.732050807568877
richtmeyermeshkov_samples_variance_0hdf5Display.Slice = 255

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
richtmeyermeshkov_samples_variance_0hdf5Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5Display.DataAxesGrid.XTitleFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5Display.DataAxesGrid.YTitleFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5Display.DataAxesGrid.ZTitleFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5Display.DataAxesGrid.XLabelFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5Display.DataAxesGrid.YLabelFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
richtmeyermeshkov_samples_variance_0hdf5Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5Display.PolarAxes.PolarAxisTitleFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5Display.PolarAxes.PolarAxisLabelFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5Display.PolarAxes.LastRadialAxisTextFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(richtmeyermeshkov_samples_variance_0hdf5Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
richtmeyermeshkov_samples_variance_0hdf5Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
richtmeyermeshkov_samples_variance_0hdf5Display.SetScalarBarVisibility(renderView1, True)

# change representation type
richtmeyermeshkov_samples_variance_0hdf5Display.SetRepresentationType('Volume')

# rescale color and/or opacity maps used to exactly fit the current data range
richtmeyermeshkov_samples_variance_0hdf5Display.RescaleTransferFunctionToDataRange(False, True)

# Properties modified on rhoPWF
rhoPWF.Points = [5.480625623022206e-05, 0.0, 0.5, 0.0, 0.07703012973070145, 0.014705882407724857, 0.5, 0.0, 0.4533539414405823, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [5.480625623022206e-05, 0.0, 0.5, 0.0, 0.07703012973070145, 0.022058824077248573, 0.5, 0.0, 0.4533539414405823, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [5.480625623022206e-05, 0.0, 0.5, 0.0, 0.07275371998548508, 0.036764707416296005, 0.5, 0.0, 0.4533539414405823, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [5.480625623022206e-05, 0.0, 0.5, 0.0, 0.07275371998548508, 0.04411764815449715, 0.5, 0.0, 0.4533539414405823, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [5.480625623022206e-05, 0.0, 0.5, 0.0, 0.06990278512239456, 0.0882352963089943, 0.5, 0.0, 0.4533539414405823, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [5.480625623022206e-05, 0.0, 0.5, 0.0, 0.06990278512239456, 0.09558823704719543, 0.5, 0.0, 0.4533539414405823, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [5.480625623022206e-05, 0.0, 0.5, 0.0, 0.06990278512239456, 0.10294117778539658, 0.5, 0.0, 0.4533539414405823, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [5.480625623022206e-05, 0.0, 0.5, 0.0, 0.06990278512239456, 0.125, 0.5, 0.0, 0.4533539414405823, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [5.480625623022206e-05, 0.0, 0.5, 0.0, 0.0684773176908493, 0.13235294818878174, 0.5, 0.0, 0.4533539414405823, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [5.480625623022206e-05, 0.0, 0.5, 0.0, 0.0684773176908493, 0.13970588147640228, 0.5, 0.0, 0.4533539414405823, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [5.480625623022206e-05, 0.0, 0.5, 0.0, 0.06134996935725212, 0.18382352590560913, 0.5, 0.0, 0.4533539414405823, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [5.480625623022206e-05, 0.0, 0.5, 0.0, 0.058499034494161606, 0.1985294073820114, 0.5, 0.0, 0.4533539414405823, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [5.480625623022206e-05, 0.0, 0.5, 0.0, 0.058499034494161606, 0.19117647409439087, 0.5, 0.0, 0.4533539414405823, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [5.480625623022206e-05, 0.0, 0.5, 0.0, 0.058499034494161606, 0.18382352590560913, 0.5, 0.0, 0.4533539414405823, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [5.480625623022206e-05, 0.0, 0.5, 0.0, 0.05992450192570686, 0.1617647111415863, 0.5, 0.0, 0.4533539414405823, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [5.480625623022206e-05, 0.0, 0.5, 0.0, 0.06134996935725212, 0.1617647111415863, 0.5, 0.0, 0.4533539414405823, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [5.480625623022206e-05, 0.0, 0.5, 0.0, 0.06134996935725212, 0.15441176295280457, 0.5, 0.0, 0.4533539414405823, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [5.480625623022206e-05, 0.0, 0.5, 0.0, 0.06277544051408768, 0.15441176295280457, 0.5, 0.0, 0.4533539414405823, 1.0, 0.5, 0.0]

# Properties modified on rhoPWF
rhoPWF.Points = [5.480625623022206e-05, 0.0, 0.5, 0.0, 0.4533539414405823, 1.0, 0.5, 0.0]

# current camera placement for renderView1
renderView1.CameraPosition = [-868.5819039716862, 1275.9312669828573, -531.0814765786998]
renderView1.CameraFocalPoint = [255.5, 255.5, 255.5]
renderView1.CameraViewUp = [-0.4383012310895304, -0.799467568808763, -0.4107841735612608]
renderView1.CameraParallelScale = 442.53898133384814

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/rm/stats/rm_variance_512_eps_005_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
richtmeyermeshkov_samples_variance_0hdf5_1 = NetCDFReader(FileName=['/scratch/snx3000/klye/richtmeyermeshkovstats/p0_05/N256/richtmeyermeshkov_samples_variance_0.hdf5'])
richtmeyermeshkov_samples_variance_0hdf5_1.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(richtmeyermeshkov_samples_variance_0hdf5, renderView1)

# set active source
SetActiveSource(richtmeyermeshkov_samples_variance_0hdf5_1)

# show data in view
richtmeyermeshkov_samples_variance_0hdf5_1Display = Show(richtmeyermeshkov_samples_variance_0hdf5_1, renderView1)

# trace defaults for the display properties.
richtmeyermeshkov_samples_variance_0hdf5_1Display.Representation = 'Outline'
richtmeyermeshkov_samples_variance_0hdf5_1Display.ColorArrayName = [None, '']
richtmeyermeshkov_samples_variance_0hdf5_1Display.OSPRayScaleArray = 'E'
richtmeyermeshkov_samples_variance_0hdf5_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
richtmeyermeshkov_samples_variance_0hdf5_1Display.SelectOrientationVectors = 'E'
richtmeyermeshkov_samples_variance_0hdf5_1Display.ScaleFactor = 25.5
richtmeyermeshkov_samples_variance_0hdf5_1Display.SelectScaleArray = 'E'
richtmeyermeshkov_samples_variance_0hdf5_1Display.GlyphType = 'Arrow'
richtmeyermeshkov_samples_variance_0hdf5_1Display.GlyphTableIndexArray = 'E'
richtmeyermeshkov_samples_variance_0hdf5_1Display.GaussianRadius = 1.2750000000000001
richtmeyermeshkov_samples_variance_0hdf5_1Display.SetScaleArray = ['POINTS', 'E']
richtmeyermeshkov_samples_variance_0hdf5_1Display.ScaleTransferFunction = 'PiecewiseFunction'
richtmeyermeshkov_samples_variance_0hdf5_1Display.OpacityArray = ['POINTS', 'E']
richtmeyermeshkov_samples_variance_0hdf5_1Display.OpacityTransferFunction = 'PiecewiseFunction'
richtmeyermeshkov_samples_variance_0hdf5_1Display.DataAxesGrid = 'GridAxesRepresentation'
richtmeyermeshkov_samples_variance_0hdf5_1Display.SelectionCellLabelFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_1Display.SelectionPointLabelFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_1Display.PolarAxes = 'PolarAxesRepresentation'
richtmeyermeshkov_samples_variance_0hdf5_1Display.ScalarOpacityUnitDistance = 1.7320508075688774
richtmeyermeshkov_samples_variance_0hdf5_1Display.Slice = 127

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
richtmeyermeshkov_samples_variance_0hdf5_1Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_1Display.DataAxesGrid.XTitleFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_1Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_1Display.DataAxesGrid.YTitleFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_1Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_1Display.DataAxesGrid.ZTitleFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_1Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_1Display.DataAxesGrid.XLabelFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_1Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_1Display.DataAxesGrid.YLabelFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_1Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
richtmeyermeshkov_samples_variance_0hdf5_1Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_1Display.PolarAxes.PolarAxisTitleFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_1Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_1Display.PolarAxes.PolarAxisLabelFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_1Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_1Display.PolarAxes.LastRadialAxisTextFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# set scalar coloring
ColorBy(richtmeyermeshkov_samples_variance_0hdf5_1Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
richtmeyermeshkov_samples_variance_0hdf5_1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
richtmeyermeshkov_samples_variance_0hdf5_1Display.SetScalarBarVisibility(renderView1, True)

# change representation type
richtmeyermeshkov_samples_variance_0hdf5_1Display.SetRepresentationType('Volume')

# current camera placement for renderView1
renderView1.CameraPosition = [-433.44106753968697, 636.717168455242, -265.02108909504597]
renderView1.CameraFocalPoint = [127.5, 127.5, 127.5]
renderView1.CameraViewUp = [-0.4383012310895304, -0.799467568808763, -0.4107841735612608]
renderView1.CameraParallelScale = 220.83647796503186

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/rm/stats/rm_variance_256_eps_005_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
richtmeyermeshkov_samples_variance_0hdf5_2 = NetCDFReader(FileName=['/scratch/snx3000/klye/richtmeyermeshkovstats/p0_05/N128/richtmeyermeshkov_samples_variance_0.hdf5'])
richtmeyermeshkov_samples_variance_0hdf5_2.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(richtmeyermeshkov_samples_variance_0hdf5_1, renderView1)

# show data in view
richtmeyermeshkov_samples_variance_0hdf5_2Display = Show(richtmeyermeshkov_samples_variance_0hdf5_2, renderView1)

# trace defaults for the display properties.
richtmeyermeshkov_samples_variance_0hdf5_2Display.Representation = 'Outline'
richtmeyermeshkov_samples_variance_0hdf5_2Display.ColorArrayName = [None, '']
richtmeyermeshkov_samples_variance_0hdf5_2Display.OSPRayScaleArray = 'E'
richtmeyermeshkov_samples_variance_0hdf5_2Display.OSPRayScaleFunction = 'PiecewiseFunction'
richtmeyermeshkov_samples_variance_0hdf5_2Display.SelectOrientationVectors = 'E'
richtmeyermeshkov_samples_variance_0hdf5_2Display.ScaleFactor = 12.700000000000001
richtmeyermeshkov_samples_variance_0hdf5_2Display.SelectScaleArray = 'E'
richtmeyermeshkov_samples_variance_0hdf5_2Display.GlyphType = 'Arrow'
richtmeyermeshkov_samples_variance_0hdf5_2Display.GlyphTableIndexArray = 'E'
richtmeyermeshkov_samples_variance_0hdf5_2Display.GaussianRadius = 0.635
richtmeyermeshkov_samples_variance_0hdf5_2Display.SetScaleArray = ['POINTS', 'E']
richtmeyermeshkov_samples_variance_0hdf5_2Display.ScaleTransferFunction = 'PiecewiseFunction'
richtmeyermeshkov_samples_variance_0hdf5_2Display.OpacityArray = ['POINTS', 'E']
richtmeyermeshkov_samples_variance_0hdf5_2Display.OpacityTransferFunction = 'PiecewiseFunction'
richtmeyermeshkov_samples_variance_0hdf5_2Display.DataAxesGrid = 'GridAxesRepresentation'
richtmeyermeshkov_samples_variance_0hdf5_2Display.SelectionCellLabelFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_2Display.SelectionPointLabelFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_2Display.PolarAxes = 'PolarAxesRepresentation'
richtmeyermeshkov_samples_variance_0hdf5_2Display.ScalarOpacityUnitDistance = 1.732050807568877
richtmeyermeshkov_samples_variance_0hdf5_2Display.Slice = 63

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
richtmeyermeshkov_samples_variance_0hdf5_2Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_2Display.DataAxesGrid.XTitleFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_2Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_2Display.DataAxesGrid.YTitleFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_2Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_2Display.DataAxesGrid.ZTitleFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_2Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_2Display.DataAxesGrid.XLabelFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_2Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_2Display.DataAxesGrid.YLabelFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_2Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_2Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
richtmeyermeshkov_samples_variance_0hdf5_2Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_2Display.PolarAxes.PolarAxisTitleFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_2Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_2Display.PolarAxes.PolarAxisLabelFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_2Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_2Display.PolarAxes.LastRadialAxisTextFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_2Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# show data in view
richtmeyermeshkov_samples_variance_0hdf5_1Display = Show(richtmeyermeshkov_samples_variance_0hdf5_1, renderView1)

# show color bar/color legend
richtmeyermeshkov_samples_variance_0hdf5_1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# hide data in view
Hide(richtmeyermeshkov_samples_variance_0hdf5_1, renderView1)

# set scalar coloring
ColorBy(richtmeyermeshkov_samples_variance_0hdf5_2Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
richtmeyermeshkov_samples_variance_0hdf5_2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
richtmeyermeshkov_samples_variance_0hdf5_2Display.SetScalarBarVisibility(renderView1, True)

# change representation type
richtmeyermeshkov_samples_variance_0hdf5_2Display.SetRepresentationType('Volume')

# set active source
SetActiveSource(richtmeyermeshkov_samples_variance_0hdf5)

# destroy richtmeyermeshkov_samples_variance_0hdf5
Delete(richtmeyermeshkov_samples_variance_0hdf5)
del richtmeyermeshkov_samples_variance_0hdf5

# set active source
SetActiveSource(richtmeyermeshkov_samples_variance_0hdf5_1)

# destroy richtmeyermeshkov_samples_variance_0hdf5_1
Delete(richtmeyermeshkov_samples_variance_0hdf5_1)
del richtmeyermeshkov_samples_variance_0hdf5_1

# set active source
SetActiveSource(richtmeyermeshkov_samples_variance_0hdf5_2)

# destroy richtmeyermeshkov_samples_variance_0hdf5_2
Delete(richtmeyermeshkov_samples_variance_0hdf5_2)
del richtmeyermeshkov_samples_variance_0hdf5_2

# create a new 'NetCDF Reader'
richtmeyermeshkov_samples_variance_0hdf5 = NetCDFReader(FileName=['/scratch/snx3000/klye/richtmeyermeshkovstats/p0_05/N512/richtmeyermeshkov_samples_variance_0.hdf5'])
richtmeyermeshkov_samples_variance_0hdf5.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# show data in view
richtmeyermeshkov_samples_variance_0hdf5Display = Show(richtmeyermeshkov_samples_variance_0hdf5, renderView1)

# trace defaults for the display properties.
richtmeyermeshkov_samples_variance_0hdf5Display.Representation = 'Outline'
richtmeyermeshkov_samples_variance_0hdf5Display.ColorArrayName = [None, '']
richtmeyermeshkov_samples_variance_0hdf5Display.OSPRayScaleArray = 'E'
richtmeyermeshkov_samples_variance_0hdf5Display.OSPRayScaleFunction = 'PiecewiseFunction'
richtmeyermeshkov_samples_variance_0hdf5Display.SelectOrientationVectors = 'E'
richtmeyermeshkov_samples_variance_0hdf5Display.ScaleFactor = 51.1
richtmeyermeshkov_samples_variance_0hdf5Display.SelectScaleArray = 'E'
richtmeyermeshkov_samples_variance_0hdf5Display.GlyphType = 'Arrow'
richtmeyermeshkov_samples_variance_0hdf5Display.GlyphTableIndexArray = 'E'
richtmeyermeshkov_samples_variance_0hdf5Display.GaussianRadius = 2.555
richtmeyermeshkov_samples_variance_0hdf5Display.SetScaleArray = ['POINTS', 'E']
richtmeyermeshkov_samples_variance_0hdf5Display.ScaleTransferFunction = 'PiecewiseFunction'
richtmeyermeshkov_samples_variance_0hdf5Display.OpacityArray = ['POINTS', 'E']
richtmeyermeshkov_samples_variance_0hdf5Display.OpacityTransferFunction = 'PiecewiseFunction'
richtmeyermeshkov_samples_variance_0hdf5Display.DataAxesGrid = 'GridAxesRepresentation'
richtmeyermeshkov_samples_variance_0hdf5Display.SelectionCellLabelFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5Display.SelectionPointLabelFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5Display.PolarAxes = 'PolarAxesRepresentation'
richtmeyermeshkov_samples_variance_0hdf5Display.ScalarOpacityUnitDistance = 1.732050807568877
richtmeyermeshkov_samples_variance_0hdf5Display.Slice = 255

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
richtmeyermeshkov_samples_variance_0hdf5Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5Display.DataAxesGrid.XTitleFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5Display.DataAxesGrid.YTitleFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5Display.DataAxesGrid.ZTitleFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5Display.DataAxesGrid.XLabelFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5Display.DataAxesGrid.YLabelFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
richtmeyermeshkov_samples_variance_0hdf5Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5Display.PolarAxes.PolarAxisTitleFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5Display.PolarAxes.PolarAxisLabelFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5Display.PolarAxes.LastRadialAxisTextFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(richtmeyermeshkov_samples_variance_0hdf5Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
richtmeyermeshkov_samples_variance_0hdf5Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
richtmeyermeshkov_samples_variance_0hdf5Display.SetScalarBarVisibility(renderView1, True)

# change representation type
richtmeyermeshkov_samples_variance_0hdf5Display.SetRepresentationType('Volume')

# current camera placement for renderView1
renderView1.CameraPosition = [-670.2051264688813, -1177.4996919581863, 140.90323544462123]
renderView1.CameraFocalPoint = [255.49999999999983, 255.50000000000006, 255.49999999999994]
renderView1.CameraViewUp = [0.3519226461829361, -0.2982903927862146, 0.8872278696451357]
renderView1.CameraParallelScale = 442.53898133384814

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/rm/stats/rm_variance_512_eps_005_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
richtmeyermeshkov_samples_variance_0hdf5_1 = NetCDFReader(FileName=['/scratch/snx3000/klye/richtmeyermeshkovstats/p0_05/N256/richtmeyermeshkov_samples_variance_0.hdf5'])
richtmeyermeshkov_samples_variance_0hdf5_1.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(richtmeyermeshkov_samples_variance_0hdf5, renderView1)

# show data in view
richtmeyermeshkov_samples_variance_0hdf5_1Display = Show(richtmeyermeshkov_samples_variance_0hdf5_1, renderView1)

# trace defaults for the display properties.
richtmeyermeshkov_samples_variance_0hdf5_1Display.Representation = 'Outline'
richtmeyermeshkov_samples_variance_0hdf5_1Display.ColorArrayName = [None, '']
richtmeyermeshkov_samples_variance_0hdf5_1Display.OSPRayScaleArray = 'E'
richtmeyermeshkov_samples_variance_0hdf5_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
richtmeyermeshkov_samples_variance_0hdf5_1Display.SelectOrientationVectors = 'E'
richtmeyermeshkov_samples_variance_0hdf5_1Display.ScaleFactor = 25.5
richtmeyermeshkov_samples_variance_0hdf5_1Display.SelectScaleArray = 'E'
richtmeyermeshkov_samples_variance_0hdf5_1Display.GlyphType = 'Arrow'
richtmeyermeshkov_samples_variance_0hdf5_1Display.GlyphTableIndexArray = 'E'
richtmeyermeshkov_samples_variance_0hdf5_1Display.GaussianRadius = 1.2750000000000001
richtmeyermeshkov_samples_variance_0hdf5_1Display.SetScaleArray = ['POINTS', 'E']
richtmeyermeshkov_samples_variance_0hdf5_1Display.ScaleTransferFunction = 'PiecewiseFunction'
richtmeyermeshkov_samples_variance_0hdf5_1Display.OpacityArray = ['POINTS', 'E']
richtmeyermeshkov_samples_variance_0hdf5_1Display.OpacityTransferFunction = 'PiecewiseFunction'
richtmeyermeshkov_samples_variance_0hdf5_1Display.DataAxesGrid = 'GridAxesRepresentation'
richtmeyermeshkov_samples_variance_0hdf5_1Display.SelectionCellLabelFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_1Display.SelectionPointLabelFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_1Display.PolarAxes = 'PolarAxesRepresentation'
richtmeyermeshkov_samples_variance_0hdf5_1Display.ScalarOpacityUnitDistance = 1.7320508075688774
richtmeyermeshkov_samples_variance_0hdf5_1Display.Slice = 127

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
richtmeyermeshkov_samples_variance_0hdf5_1Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_1Display.DataAxesGrid.XTitleFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_1Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_1Display.DataAxesGrid.YTitleFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_1Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_1Display.DataAxesGrid.ZTitleFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_1Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_1Display.DataAxesGrid.XLabelFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_1Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_1Display.DataAxesGrid.YLabelFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_1Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
richtmeyermeshkov_samples_variance_0hdf5_1Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_1Display.PolarAxes.PolarAxisTitleFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_1Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_1Display.PolarAxes.PolarAxisLabelFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_1Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_1Display.PolarAxes.LastRadialAxisTextFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(richtmeyermeshkov_samples_variance_0hdf5_1Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
richtmeyermeshkov_samples_variance_0hdf5_1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
richtmeyermeshkov_samples_variance_0hdf5_1Display.SetScalarBarVisibility(renderView1, True)

# change representation type
richtmeyermeshkov_samples_variance_0hdf5_1Display.SetRepresentationType('Volume')

# current camera placement for renderView1
renderView1.CameraPosition = [-334.44678522419656, -587.5976936386244, 70.31374762892068]
renderView1.CameraFocalPoint = [127.5, 127.5, 127.5]
renderView1.CameraViewUp = [0.3519226461829361, -0.2982903927862146, 0.8872278696451357]
renderView1.CameraParallelScale = 220.83647796503186

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/rm/stats/rm_variance_256_eps_005_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
richtmeyermeshkov_samples_variance_0hdf5_2 = NetCDFReader(FileName=['/scratch/snx3000/klye/richtmeyermeshkovstats/p0_05/N128/richtmeyermeshkov_samples_variance_0.hdf5'])
richtmeyermeshkov_samples_variance_0hdf5_2.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(richtmeyermeshkov_samples_variance_0hdf5_1, renderView1)

# show data in view
richtmeyermeshkov_samples_variance_0hdf5_2Display = Show(richtmeyermeshkov_samples_variance_0hdf5_2, renderView1)

# trace defaults for the display properties.
richtmeyermeshkov_samples_variance_0hdf5_2Display.Representation = 'Outline'
richtmeyermeshkov_samples_variance_0hdf5_2Display.ColorArrayName = [None, '']
richtmeyermeshkov_samples_variance_0hdf5_2Display.OSPRayScaleArray = 'E'
richtmeyermeshkov_samples_variance_0hdf5_2Display.OSPRayScaleFunction = 'PiecewiseFunction'
richtmeyermeshkov_samples_variance_0hdf5_2Display.SelectOrientationVectors = 'E'
richtmeyermeshkov_samples_variance_0hdf5_2Display.ScaleFactor = 12.700000000000001
richtmeyermeshkov_samples_variance_0hdf5_2Display.SelectScaleArray = 'E'
richtmeyermeshkov_samples_variance_0hdf5_2Display.GlyphType = 'Arrow'
richtmeyermeshkov_samples_variance_0hdf5_2Display.GlyphTableIndexArray = 'E'
richtmeyermeshkov_samples_variance_0hdf5_2Display.GaussianRadius = 0.635
richtmeyermeshkov_samples_variance_0hdf5_2Display.SetScaleArray = ['POINTS', 'E']
richtmeyermeshkov_samples_variance_0hdf5_2Display.ScaleTransferFunction = 'PiecewiseFunction'
richtmeyermeshkov_samples_variance_0hdf5_2Display.OpacityArray = ['POINTS', 'E']
richtmeyermeshkov_samples_variance_0hdf5_2Display.OpacityTransferFunction = 'PiecewiseFunction'
richtmeyermeshkov_samples_variance_0hdf5_2Display.DataAxesGrid = 'GridAxesRepresentation'
richtmeyermeshkov_samples_variance_0hdf5_2Display.SelectionCellLabelFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_2Display.SelectionPointLabelFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_2Display.PolarAxes = 'PolarAxesRepresentation'
richtmeyermeshkov_samples_variance_0hdf5_2Display.ScalarOpacityUnitDistance = 1.732050807568877
richtmeyermeshkov_samples_variance_0hdf5_2Display.Slice = 63

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
richtmeyermeshkov_samples_variance_0hdf5_2Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_2Display.DataAxesGrid.XTitleFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_2Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_2Display.DataAxesGrid.YTitleFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_2Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_2Display.DataAxesGrid.ZTitleFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_2Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_2Display.DataAxesGrid.XLabelFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_2Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_2Display.DataAxesGrid.YLabelFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_2Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_2Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
richtmeyermeshkov_samples_variance_0hdf5_2Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_2Display.PolarAxes.PolarAxisTitleFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_2Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_2Display.PolarAxes.PolarAxisLabelFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_2Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_2Display.PolarAxes.LastRadialAxisTextFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_2Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(richtmeyermeshkov_samples_variance_0hdf5_2Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
richtmeyermeshkov_samples_variance_0hdf5_2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
richtmeyermeshkov_samples_variance_0hdf5_2Display.SetScalarBarVisibility(renderView1, True)

# change representation type
richtmeyermeshkov_samples_variance_0hdf5_2Display.SetRepresentationType('Volume')

# current camera placement for renderView1
renderView1.CameraPosition = [-166.56761460185476, -292.6466944788443, 35.0190037210703]
renderView1.CameraFocalPoint = [63.5, 63.5, 63.5]
renderView1.CameraViewUp = [0.3519226461829361, -0.2982903927862146, 0.8872278696451357]
renderView1.CameraParallelScale = 109.9852262806237

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/rm/stats/rm_variance_128_eps_005_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
richtmeyermeshkov_samples_variance_0hdf5_3 = NetCDFReader(FileName=['/scratch/snx3000/klye/richtmeyermeshkovstats/p0_05/N64/richtmeyermeshkov_samples_variance_0.hdf5'])
richtmeyermeshkov_samples_variance_0hdf5_3.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(richtmeyermeshkov_samples_variance_0hdf5_2, renderView1)

# show data in view
richtmeyermeshkov_samples_variance_0hdf5_3Display = Show(richtmeyermeshkov_samples_variance_0hdf5_3, renderView1)

# trace defaults for the display properties.
richtmeyermeshkov_samples_variance_0hdf5_3Display.Representation = 'Outline'
richtmeyermeshkov_samples_variance_0hdf5_3Display.ColorArrayName = [None, '']
richtmeyermeshkov_samples_variance_0hdf5_3Display.OSPRayScaleArray = 'E'
richtmeyermeshkov_samples_variance_0hdf5_3Display.OSPRayScaleFunction = 'PiecewiseFunction'
richtmeyermeshkov_samples_variance_0hdf5_3Display.SelectOrientationVectors = 'E'
richtmeyermeshkov_samples_variance_0hdf5_3Display.ScaleFactor = 6.300000000000001
richtmeyermeshkov_samples_variance_0hdf5_3Display.SelectScaleArray = 'E'
richtmeyermeshkov_samples_variance_0hdf5_3Display.GlyphType = 'Arrow'
richtmeyermeshkov_samples_variance_0hdf5_3Display.GlyphTableIndexArray = 'E'
richtmeyermeshkov_samples_variance_0hdf5_3Display.GaussianRadius = 0.315
richtmeyermeshkov_samples_variance_0hdf5_3Display.SetScaleArray = ['POINTS', 'E']
richtmeyermeshkov_samples_variance_0hdf5_3Display.ScaleTransferFunction = 'PiecewiseFunction'
richtmeyermeshkov_samples_variance_0hdf5_3Display.OpacityArray = ['POINTS', 'E']
richtmeyermeshkov_samples_variance_0hdf5_3Display.OpacityTransferFunction = 'PiecewiseFunction'
richtmeyermeshkov_samples_variance_0hdf5_3Display.DataAxesGrid = 'GridAxesRepresentation'
richtmeyermeshkov_samples_variance_0hdf5_3Display.SelectionCellLabelFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_3Display.SelectionPointLabelFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_3Display.PolarAxes = 'PolarAxesRepresentation'
richtmeyermeshkov_samples_variance_0hdf5_3Display.ScalarOpacityUnitDistance = 1.7320508075688774
richtmeyermeshkov_samples_variance_0hdf5_3Display.Slice = 31

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
richtmeyermeshkov_samples_variance_0hdf5_3Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_3Display.DataAxesGrid.XTitleFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_3Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_3Display.DataAxesGrid.YTitleFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_3Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_3Display.DataAxesGrid.ZTitleFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_3Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_3Display.DataAxesGrid.XLabelFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_3Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_3Display.DataAxesGrid.YLabelFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_3Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_3Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
richtmeyermeshkov_samples_variance_0hdf5_3Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_3Display.PolarAxes.PolarAxisTitleFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_3Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_3Display.PolarAxes.PolarAxisLabelFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_3Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_3Display.PolarAxes.LastRadialAxisTextFontFile = ''
richtmeyermeshkov_samples_variance_0hdf5_3Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
richtmeyermeshkov_samples_variance_0hdf5_3Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(richtmeyermeshkov_samples_variance_0hdf5_3Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
richtmeyermeshkov_samples_variance_0hdf5_3Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
richtmeyermeshkov_samples_variance_0hdf5_3Display.SetScalarBarVisibility(renderView1, True)

# change representation type
richtmeyermeshkov_samples_variance_0hdf5_3Display.SetRepresentationType('Volume')

# current camera placement for renderView1
renderView1.CameraPosition = [-82.62802929068387, -145.1711948989543, 17.371631767145104]
renderView1.CameraFocalPoint = [31.5, 31.5, 31.5]
renderView1.CameraViewUp = [0.3519226461829361, -0.2982903927862146, 0.8872278696451357]
renderView1.CameraParallelScale = 54.559600438419636

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/rm/stats/rm_variance_64_eps_005_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# hide data in view
Hide(richtmeyermeshkov_samples_variance_0hdf5_3, renderView1)

# create a new 'NetCDF Reader'
rm_cuda_0hdf5 = NetCDFReader(FileName=['/scratch/snx3000/klye/richtmeyermeshkovstats/p0_05/N512/rm_cuda_0.hdf5'])
rm_cuda_0hdf5.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# show data in view
rm_cuda_0hdf5Display = Show(rm_cuda_0hdf5, renderView1)

# trace defaults for the display properties.
rm_cuda_0hdf5Display.Representation = 'Outline'
rm_cuda_0hdf5Display.ColorArrayName = [None, '']
rm_cuda_0hdf5Display.OSPRayScaleArray = 'sample_0_E'
rm_cuda_0hdf5Display.OSPRayScaleFunction = 'PiecewiseFunction'
rm_cuda_0hdf5Display.SelectOrientationVectors = 'None'
rm_cuda_0hdf5Display.ScaleFactor = 51.1
rm_cuda_0hdf5Display.SelectScaleArray = 'None'
rm_cuda_0hdf5Display.GlyphType = 'Arrow'
rm_cuda_0hdf5Display.GlyphTableIndexArray = 'None'
rm_cuda_0hdf5Display.GaussianRadius = 2.555
rm_cuda_0hdf5Display.SetScaleArray = ['POINTS', 'sample_0_E']
rm_cuda_0hdf5Display.ScaleTransferFunction = 'PiecewiseFunction'
rm_cuda_0hdf5Display.OpacityArray = ['POINTS', 'sample_0_E']
rm_cuda_0hdf5Display.OpacityTransferFunction = 'PiecewiseFunction'
rm_cuda_0hdf5Display.DataAxesGrid = 'GridAxesRepresentation'
rm_cuda_0hdf5Display.SelectionCellLabelFontFile = ''
rm_cuda_0hdf5Display.SelectionPointLabelFontFile = ''
rm_cuda_0hdf5Display.PolarAxes = 'PolarAxesRepresentation'
rm_cuda_0hdf5Display.ScalarOpacityUnitDistance = 1.732050807568877
rm_cuda_0hdf5Display.Slice = 255

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
rm_cuda_0hdf5Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
rm_cuda_0hdf5Display.DataAxesGrid.XTitleFontFile = ''
rm_cuda_0hdf5Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
rm_cuda_0hdf5Display.DataAxesGrid.YTitleFontFile = ''
rm_cuda_0hdf5Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
rm_cuda_0hdf5Display.DataAxesGrid.ZTitleFontFile = ''
rm_cuda_0hdf5Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
rm_cuda_0hdf5Display.DataAxesGrid.XLabelFontFile = ''
rm_cuda_0hdf5Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
rm_cuda_0hdf5Display.DataAxesGrid.YLabelFontFile = ''
rm_cuda_0hdf5Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
rm_cuda_0hdf5Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
rm_cuda_0hdf5Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
rm_cuda_0hdf5Display.PolarAxes.PolarAxisTitleFontFile = ''
rm_cuda_0hdf5Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
rm_cuda_0hdf5Display.PolarAxes.PolarAxisLabelFontFile = ''
rm_cuda_0hdf5Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
rm_cuda_0hdf5Display.PolarAxes.LastRadialAxisTextFontFile = ''
rm_cuda_0hdf5Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
rm_cuda_0hdf5Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(rm_cuda_0hdf5Display, ('POINTS', 'sample_0_rho'))

# rescale color and/or opacity maps used to include current data range
rm_cuda_0hdf5Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
rm_cuda_0hdf5Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'sample_0_rho'
sample_0_rhoLUT = GetColorTransferFunction('sample_0_rho')
sample_0_rhoLUT.RGBPoints = [0.26437944173812866, 0.231373, 0.298039, 0.752941, 1.6165518462657928, 0.865003, 0.865003, 0.865003, 2.968724250793457, 0.705882, 0.0156863, 0.14902]
sample_0_rhoLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'sample_0_rho'
sample_0_rhoPWF = GetOpacityTransferFunction('sample_0_rho')
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]
sample_0_rhoPWF.ScalarRangeInitialized = 1

# change representation type
rm_cuda_0hdf5Display.SetRepresentationType('Volume')

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
sample_0_rhoLUT.ApplyPreset('Viridis (matplotlib)', True)

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.6165517568588257, 0.4852941334247589, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.6250560283660889, 0.45588234066963196, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.6250560283660889, 0.4485294222831726, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.633560299873352, 0.44117647409439087, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.6420644521713257, 0.4117647111415863, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.6505687236785889, 0.3970588147640228, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.6505687236785889, 0.3897058963775635, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.6675771474838257, 0.38235294818878174, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.6760814189910889, 0.375, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.6930898427963257, 0.36764705181121826, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.7015941143035889, 0.3602941334247589, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.7100982666015625, 0.34558823704719543, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.7100982666015625, 0.3382352888584137, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.7271068096160889, 0.33088234066963196, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.7356109619140625, 0.30882352590560913, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.7526195049285889, 0.27941176295280457, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.7696279287338257, 0.25, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.7951406240463257, 0.20588235557079315, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.8036447763442993, 0.1764705926179886, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.8121490478515625, 0.1617647111415863, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.8121490478515625, 0.14705882966518402, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.8206533193588257, 0.13235294818878174, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.8206533193588257, 0.125, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.8206533193588257, 0.11764705926179886, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.8291574716567993, 0.10294117778539658, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.8291574716567993, 0.09558823704719543, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.8291574716567993, 0.0882352963089943, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.8291574716567993, 0.08088235557079315, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.8291574716567993, 0.05882352963089943, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.8291574716567993, 0.05147058889269829, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.8206533193588257, 0.029411764815449715, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.8121490478515625, 0.0, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.8036447763442993, 0.0, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.7951406240463257, 0.0, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.7696279287338257, 0.0, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.7611236572265625, 0.0, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.7441152334213257, 0.014705882407724857, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.7356109619140625, 0.029411764815449715, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.7271068096160889, 0.036764707416296005, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.7271068096160889, 0.04411764815449715, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.7186025381088257, 0.05147058889269829, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.7015941143035889, 0.06617647409439087, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.7015941143035889, 0.07352941483259201, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.7015941143035889, 0.08088235557079315, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.6930898427963257, 0.08088235557079315, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.6845855712890625, 0.08088235557079315, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.6760814189910889, 0.08088235557079315, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.6165517568588257, 0.11764705926179886, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.6505687236785889, 0.11764705926179886, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.659072995185852, 0.11764705926179886, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.6675771474838257, 0.11764705926179886, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.6760814189910889, 0.11764705926179886, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.6760814189910889, 0.11029411852359772, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.6845855712890625, 0.11029411852359772, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.6930898427963257, 0.11029411852359772, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.7015941143035889, 0.11029411852359772, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.7015941143035889, 0.09558823704719543, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.6845855712890625, 0.09558823704719543, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.633560299873352, 0.20588235557079315, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.6250560283660889, 0.23529411852359772, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.6250560283660889, 0.24264706671237946, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.6165517568588257, 0.2720588147640228, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.6165517568588257, 0.2867647111415863, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.6165517568588257, 0.29411765933036804, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.6165517568588257, 0.30882352590560913, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.6165517568588257, 0.31617647409439087, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.6165517568588257, 0.3235294222831726, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.6165517568588257, 0.33088234066963196, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.6165517568588257, 0.34558823704719543, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.6165517568588257, 0.3529411852359772, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.6250560283660889, 0.4264705777168274, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.26437944173812866, 0.0, 0.5, 0.0, 1.633560299873352, 0.4264705777168274, 0.5, 0.0, 2.968724250793457, 1.0, 0.5, 0.0]

# Rescale transfer function
sample_0_rhoLUT.RescaleTransferFunction(1.1, 2.96872425079)

# Rescale transfer function
sample_0_rhoPWF.RescaleTransferFunction(1.1, 2.96872425079)

# Rescale transfer function
sample_0_rhoLUT.RescaleTransferFunction(1.2, 2.96872425079)

# Rescale transfer function
sample_0_rhoPWF.RescaleTransferFunction(1.2, 2.96872425079)

# current camera placement for renderView1
renderView1.CameraPosition = [-696.5748308366443, -1163.120782859373, 187.53598234047175]
renderView1.CameraFocalPoint = [255.49999999999997, 255.49999999999991, 255.50000000000009]
renderView1.CameraViewUp = [0.35769327155260716, -0.2826972398852228, 0.8900212323575599]
renderView1.CameraParallelScale = 442.53898133384814

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/rm/single/rm_512_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
rm_cuda_0hdf5_1 = NetCDFReader(FileName=['/scratch/snx3000/klye/richtmeyermeshkovstats/p0_05/N256/rm_cuda_0.hdf5'])
rm_cuda_0hdf5_1.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(rm_cuda_0hdf5, renderView1)

# show data in view
rm_cuda_0hdf5_1Display = Show(rm_cuda_0hdf5_1, renderView1)

# trace defaults for the display properties.
rm_cuda_0hdf5_1Display.Representation = 'Outline'
rm_cuda_0hdf5_1Display.ColorArrayName = [None, '']
rm_cuda_0hdf5_1Display.OSPRayScaleArray = 'sample_0_E'
rm_cuda_0hdf5_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
rm_cuda_0hdf5_1Display.SelectOrientationVectors = 'None'
rm_cuda_0hdf5_1Display.ScaleFactor = 25.5
rm_cuda_0hdf5_1Display.SelectScaleArray = 'None'
rm_cuda_0hdf5_1Display.GlyphType = 'Arrow'
rm_cuda_0hdf5_1Display.GlyphTableIndexArray = 'None'
rm_cuda_0hdf5_1Display.GaussianRadius = 1.2750000000000001
rm_cuda_0hdf5_1Display.SetScaleArray = ['POINTS', 'sample_0_E']
rm_cuda_0hdf5_1Display.ScaleTransferFunction = 'PiecewiseFunction'
rm_cuda_0hdf5_1Display.OpacityArray = ['POINTS', 'sample_0_E']
rm_cuda_0hdf5_1Display.OpacityTransferFunction = 'PiecewiseFunction'
rm_cuda_0hdf5_1Display.DataAxesGrid = 'GridAxesRepresentation'
rm_cuda_0hdf5_1Display.SelectionCellLabelFontFile = ''
rm_cuda_0hdf5_1Display.SelectionPointLabelFontFile = ''
rm_cuda_0hdf5_1Display.PolarAxes = 'PolarAxesRepresentation'
rm_cuda_0hdf5_1Display.ScalarOpacityUnitDistance = 1.7320508075688774
rm_cuda_0hdf5_1Display.Slice = 127

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
rm_cuda_0hdf5_1Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
rm_cuda_0hdf5_1Display.DataAxesGrid.XTitleFontFile = ''
rm_cuda_0hdf5_1Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
rm_cuda_0hdf5_1Display.DataAxesGrid.YTitleFontFile = ''
rm_cuda_0hdf5_1Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
rm_cuda_0hdf5_1Display.DataAxesGrid.ZTitleFontFile = ''
rm_cuda_0hdf5_1Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
rm_cuda_0hdf5_1Display.DataAxesGrid.XLabelFontFile = ''
rm_cuda_0hdf5_1Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
rm_cuda_0hdf5_1Display.DataAxesGrid.YLabelFontFile = ''
rm_cuda_0hdf5_1Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
rm_cuda_0hdf5_1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
rm_cuda_0hdf5_1Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
rm_cuda_0hdf5_1Display.PolarAxes.PolarAxisTitleFontFile = ''
rm_cuda_0hdf5_1Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
rm_cuda_0hdf5_1Display.PolarAxes.PolarAxisLabelFontFile = ''
rm_cuda_0hdf5_1Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
rm_cuda_0hdf5_1Display.PolarAxes.LastRadialAxisTextFontFile = ''
rm_cuda_0hdf5_1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
rm_cuda_0hdf5_1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(rm_cuda_0hdf5_1Display, ('POINTS', 'sample_0_rho'))

# rescale color and/or opacity maps used to include current data range
rm_cuda_0hdf5_1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
rm_cuda_0hdf5_1Display.SetScalarBarVisibility(renderView1, True)

# change representation type
rm_cuda_0hdf5_1Display.SetRepresentationType('Volume')

# Rescale transfer function
sample_0_rhoLUT.RescaleTransferFunction(1.1, 2.96872425079)

# Rescale transfer function
sample_0_rhoPWF.RescaleTransferFunction(1.1, 2.96872425079)

# set active source
SetActiveSource(rm_cuda_0hdf5)

# set active source
SetActiveSource(rm_cuda_0hdf5_1)

# hide data in view
Hide(rm_cuda_0hdf5_1, renderView1)

# set active source
SetActiveSource(rm_cuda_0hdf5)

# show data in view
rm_cuda_0hdf5Display = Show(rm_cuda_0hdf5, renderView1)

# show color bar/color legend
rm_cuda_0hdf5Display.SetScalarBarVisibility(renderView1, True)

# reset view to fit data
renderView1.ResetCamera()

# Rescale transfer function
sample_0_rhoLUT.RescaleTransferFunction(1.1, 3.0)

# Rescale transfer function
sample_0_rhoPWF.RescaleTransferFunction(1.1, 3.0)

# current camera placement for renderView1
renderView1.CameraPosition = [-696.5748308366425, -1163.1207828593704, 187.53598234047178]
renderView1.CameraFocalPoint = [255.5, 255.5, 255.5]
renderView1.CameraViewUp = [0.35769327155260716, -0.2826972398852228, 0.8900212323575599]
renderView1.CameraParallelScale = 442.53898133384814

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/rm/single/rm_512_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# hide data in view
Hide(rm_cuda_0hdf5, renderView1)

# set active source
SetActiveSource(rm_cuda_0hdf5_1)

# show data in view
rm_cuda_0hdf5_1Display = Show(rm_cuda_0hdf5_1, renderView1)

# show color bar/color legend
rm_cuda_0hdf5_1Display.SetScalarBarVisibility(renderView1, True)

# reset view to fit data
renderView1.ResetCamera()

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [1.1, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# current camera placement for renderView1
renderView1.CameraPosition = [-347.6058353490094, -580.422308471897, 93.58449216598885]
renderView1.CameraFocalPoint = [127.5, 127.5, 127.5]
renderView1.CameraViewUp = [0.35769327155260716, -0.2826972398852228, 0.8900212323575599]
renderView1.CameraParallelScale = 220.83647796503186

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/rm/single/rm_256_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
rm_cuda_0hdf5_2 = NetCDFReader(FileName=['/scratch/snx3000/klye/richtmeyermeshkovstats/p0_05/N128/rm_cuda_0.hdf5'])
rm_cuda_0hdf5_2.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(rm_cuda_0hdf5_1, renderView1)

# set active source
SetActiveSource(rm_cuda_0hdf5_2)

# show data in view
rm_cuda_0hdf5_2Display = Show(rm_cuda_0hdf5_2, renderView1)

# trace defaults for the display properties.
rm_cuda_0hdf5_2Display.Representation = 'Outline'
rm_cuda_0hdf5_2Display.ColorArrayName = [None, '']
rm_cuda_0hdf5_2Display.OSPRayScaleArray = 'sample_0_E'
rm_cuda_0hdf5_2Display.OSPRayScaleFunction = 'PiecewiseFunction'
rm_cuda_0hdf5_2Display.SelectOrientationVectors = 'None'
rm_cuda_0hdf5_2Display.ScaleFactor = 12.700000000000001
rm_cuda_0hdf5_2Display.SelectScaleArray = 'None'
rm_cuda_0hdf5_2Display.GlyphType = 'Arrow'
rm_cuda_0hdf5_2Display.GlyphTableIndexArray = 'None'
rm_cuda_0hdf5_2Display.GaussianRadius = 0.635
rm_cuda_0hdf5_2Display.SetScaleArray = ['POINTS', 'sample_0_E']
rm_cuda_0hdf5_2Display.ScaleTransferFunction = 'PiecewiseFunction'
rm_cuda_0hdf5_2Display.OpacityArray = ['POINTS', 'sample_0_E']
rm_cuda_0hdf5_2Display.OpacityTransferFunction = 'PiecewiseFunction'
rm_cuda_0hdf5_2Display.DataAxesGrid = 'GridAxesRepresentation'
rm_cuda_0hdf5_2Display.SelectionCellLabelFontFile = ''
rm_cuda_0hdf5_2Display.SelectionPointLabelFontFile = ''
rm_cuda_0hdf5_2Display.PolarAxes = 'PolarAxesRepresentation'
rm_cuda_0hdf5_2Display.ScalarOpacityUnitDistance = 1.732050807568877
rm_cuda_0hdf5_2Display.Slice = 63

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
rm_cuda_0hdf5_2Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
rm_cuda_0hdf5_2Display.DataAxesGrid.XTitleFontFile = ''
rm_cuda_0hdf5_2Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
rm_cuda_0hdf5_2Display.DataAxesGrid.YTitleFontFile = ''
rm_cuda_0hdf5_2Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
rm_cuda_0hdf5_2Display.DataAxesGrid.ZTitleFontFile = ''
rm_cuda_0hdf5_2Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
rm_cuda_0hdf5_2Display.DataAxesGrid.XLabelFontFile = ''
rm_cuda_0hdf5_2Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
rm_cuda_0hdf5_2Display.DataAxesGrid.YLabelFontFile = ''
rm_cuda_0hdf5_2Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
rm_cuda_0hdf5_2Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
rm_cuda_0hdf5_2Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
rm_cuda_0hdf5_2Display.PolarAxes.PolarAxisTitleFontFile = ''
rm_cuda_0hdf5_2Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
rm_cuda_0hdf5_2Display.PolarAxes.PolarAxisLabelFontFile = ''
rm_cuda_0hdf5_2Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
rm_cuda_0hdf5_2Display.PolarAxes.LastRadialAxisTextFontFile = ''
rm_cuda_0hdf5_2Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
rm_cuda_0hdf5_2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# set scalar coloring
ColorBy(rm_cuda_0hdf5_2Display, ('POINTS', 'sample_0_rho'))

# rescale color and/or opacity maps used to include current data range
rm_cuda_0hdf5_2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
rm_cuda_0hdf5_2Display.SetScalarBarVisibility(renderView1, True)

# change representation type
rm_cuda_0hdf5_2Display.SetRepresentationType('Volume')

# Rescale transfer function
sample_0_rhoLUT.RescaleTransferFunction(1.1, 3.0)

# Rescale transfer function
sample_0_rhoPWF.RescaleTransferFunction(1.1, 3.0)

# current camera placement for renderView1
renderView1.CameraPosition = [-173.12133760519296, -289.0730712781605, 46.608747078747385]
renderView1.CameraFocalPoint = [63.5, 63.5, 63.5]
renderView1.CameraViewUp = [0.35769327155260716, -0.2826972398852228, 0.8900212323575599]
renderView1.CameraParallelScale = 109.9852262806237

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/rm/single/rm_128_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
rm_cuda_0hdf5_3 = NetCDFReader(FileName=['/scratch/snx3000/klye/richtmeyermeshkovstats/p0_05/N64/rm_cuda_0.hdf5'])
rm_cuda_0hdf5_3.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(rm_cuda_0hdf5_2, renderView1)

# show data in view
rm_cuda_0hdf5_2Display = Show(rm_cuda_0hdf5_2, renderView1)

# reset view to fit data
renderView1.ResetCamera()

# show color bar/color legend
rm_cuda_0hdf5_2Display.SetScalarBarVisibility(renderView1, True)

# show data in view
rm_cuda_0hdf5_3Display = Show(rm_cuda_0hdf5_3, renderView1)

# trace defaults for the display properties.
rm_cuda_0hdf5_3Display.Representation = 'Outline'
rm_cuda_0hdf5_3Display.ColorArrayName = [None, '']
rm_cuda_0hdf5_3Display.OSPRayScaleArray = 'sample_0_E'
rm_cuda_0hdf5_3Display.OSPRayScaleFunction = 'PiecewiseFunction'
rm_cuda_0hdf5_3Display.SelectOrientationVectors = 'None'
rm_cuda_0hdf5_3Display.ScaleFactor = 6.300000000000001
rm_cuda_0hdf5_3Display.SelectScaleArray = 'None'
rm_cuda_0hdf5_3Display.GlyphType = 'Arrow'
rm_cuda_0hdf5_3Display.GlyphTableIndexArray = 'None'
rm_cuda_0hdf5_3Display.GaussianRadius = 0.315
rm_cuda_0hdf5_3Display.SetScaleArray = ['POINTS', 'sample_0_E']
rm_cuda_0hdf5_3Display.ScaleTransferFunction = 'PiecewiseFunction'
rm_cuda_0hdf5_3Display.OpacityArray = ['POINTS', 'sample_0_E']
rm_cuda_0hdf5_3Display.OpacityTransferFunction = 'PiecewiseFunction'
rm_cuda_0hdf5_3Display.DataAxesGrid = 'GridAxesRepresentation'
rm_cuda_0hdf5_3Display.SelectionCellLabelFontFile = ''
rm_cuda_0hdf5_3Display.SelectionPointLabelFontFile = ''
rm_cuda_0hdf5_3Display.PolarAxes = 'PolarAxesRepresentation'
rm_cuda_0hdf5_3Display.ScalarOpacityUnitDistance = 1.7320508075688774
rm_cuda_0hdf5_3Display.Slice = 31

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
rm_cuda_0hdf5_3Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
rm_cuda_0hdf5_3Display.DataAxesGrid.XTitleFontFile = ''
rm_cuda_0hdf5_3Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
rm_cuda_0hdf5_3Display.DataAxesGrid.YTitleFontFile = ''
rm_cuda_0hdf5_3Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
rm_cuda_0hdf5_3Display.DataAxesGrid.ZTitleFontFile = ''
rm_cuda_0hdf5_3Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
rm_cuda_0hdf5_3Display.DataAxesGrid.XLabelFontFile = ''
rm_cuda_0hdf5_3Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
rm_cuda_0hdf5_3Display.DataAxesGrid.YLabelFontFile = ''
rm_cuda_0hdf5_3Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
rm_cuda_0hdf5_3Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
rm_cuda_0hdf5_3Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
rm_cuda_0hdf5_3Display.PolarAxes.PolarAxisTitleFontFile = ''
rm_cuda_0hdf5_3Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
rm_cuda_0hdf5_3Display.PolarAxes.PolarAxisLabelFontFile = ''
rm_cuda_0hdf5_3Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
rm_cuda_0hdf5_3Display.PolarAxes.LastRadialAxisTextFontFile = ''
rm_cuda_0hdf5_3Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
rm_cuda_0hdf5_3Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# update the view to ensure updated data information
renderView1.Update()

# Rescale transfer function
sample_0_rhoLUT.RescaleTransferFunction(0.200084805489, 3.0)

# Rescale transfer function
sample_0_rhoPWF.RescaleTransferFunction(0.200084805489, 3.0)

# set scalar coloring
ColorBy(rm_cuda_0hdf5_3Display, ('POINTS', 'sample_0_rho'))

# rescale color and/or opacity maps used to include current data range
rm_cuda_0hdf5_3Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
rm_cuda_0hdf5_3Display.SetScalarBarVisibility(renderView1, True)

# change representation type
rm_cuda_0hdf5_3Display.SetRepresentationType('Volume')

# hide data in view
Hide(rm_cuda_0hdf5_2, renderView1)

# hide data in view
Hide(rm_cuda_0hdf5_3, renderView1)

# set active source
SetActiveSource(rm_cuda_0hdf5_3)

# show data in view
rm_cuda_0hdf5_3Display = Show(rm_cuda_0hdf5_3, renderView1)

# show color bar/color legend
rm_cuda_0hdf5_3Display.SetScalarBarVisibility(renderView1, True)

# reset view to fit data
renderView1.ResetCamera()

# Rescale transfer function
sample_0_rhoLUT.RescaleTransferFunction(1.1, 3.0)

# Rescale transfer function
sample_0_rhoPWF.RescaleTransferFunction(1.1, 3.0)

# current camera placement for renderView1
renderView1.CameraPosition = [-85.8790887332847, -143.3984526812922, 23.120874535126653]
renderView1.CameraFocalPoint = [31.5, 31.5, 31.5]
renderView1.CameraViewUp = [0.35769327155260716, -0.2826972398852228, 0.8900212323575599]
renderView1.CameraParallelScale = 54.559600438419636

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/rm/single/rm_64_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# Rescale transfer function
sample_0_rhoLUT.RescaleTransferFunction(0.7, 3.0)

# Rescale transfer function
sample_0_rhoPWF.RescaleTransferFunction(0.7, 3.0)

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.1339622735977173, 0.22058823704719543, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.1339622735977173, 0.18382352590560913, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.1411949396133423, 0.18382352590560913, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.1411949396133423, 0.1764705926179886, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.1484276056289673, 0.10294117778539658, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.1556603908538818, 0.0882352963089943, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.1628930568695068, 0.06617647409439087, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.1628930568695068, 0.05147058889269829, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.1628930568695068, 0.04411764815449715, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.1701257228851318, 0.04411764815449715, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.199056625366211, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.206289291381836, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.206289291381836, 0.007352941203862429, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.199056625366211, 0.007352941203862429, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.199056625366211, 0.022058824077248573, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.206289291381836, 0.04411764815449715, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.199056625366211, 0.04411764815449715, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.1628930568695068, 0.05147058889269829, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.213521957397461, 0.09558823704719543, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.2207547426223755, 0.09558823704719543, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.2279874086380005, 0.09558823704719543, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.24245285987854, 0.08088235557079315, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.249685525894165, 0.08088235557079315, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.25691819190979, 0.07352941483259201, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.2641509771347046, 0.05147058889269829, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.2713836431503296, 0.04411764815449715, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.2641509771347046, 0.04411764815449715, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.2641509771347046, 0.05147058889269829, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.2641509771347046, 0.05882352963089943, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.25691819190979, 0.08088235557079315, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.25691819190979, 0.0882352963089943, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.25691819190979, 0.09558823704719543, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.249685525894165, 0.10294117778539658, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.24245285987854, 0.125, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.2352200746536255, 0.13970588147640228, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.2352200746536255, 0.14705882966518402, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.2279874086380005, 0.14705882966518402, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.2279874086380005, 0.15441176295280457, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.2207547426223755, 0.1985294073820114, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.2207547426223755, 0.1985294073820114, 0.5, 0.0, 2.479245185852051, 0.7867646813392639, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.2207547426223755, 0.1985294073820114, 0.5, 0.0, 2.472012519836426, 0.779411792755127, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.2207547426223755, 0.1985294073820114, 0.5, 0.0, 2.457547187805176, 0.7720588445663452, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.2207547426223755, 0.1985294073820114, 0.5, 0.0, 2.4213836193084717, 0.7573529481887817, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.2207547426223755, 0.1985294073820114, 0.5, 0.0, 2.4358489513397217, 0.75, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.2207547426223755, 0.1985294073820114, 0.5, 0.0, 2.3707547187805176, 1.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.2207547426223755, 0.1985294073820114, 0.5, 0.0, 2.3779873847961426, 1.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.2207547426223755, 0.1985294073820114, 0.5, 0.1538461446762085, 1.7559747695922852, 0.529411792755127, 0.5, 0.0, 2.3779873847961426, 1.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.2207547426223755, 0.1985294073820114, 0.5, 0.1538461446762085, 1.8355345726013184, 0.5441176295280457, 0.5, 0.0, 2.3779873847961426, 1.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.2207547426223755, 0.1985294073820114, 0.5, 0.1538461446762085, 1.8283019065856934, 0.5441176295280457, 0.5, 0.0, 2.3779873847961426, 1.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.2207547426223755, 0.1985294073820114, 0.5, 0.1538461446762085, 1.7921383380889893, 0.5367646813392639, 0.5, 0.0, 2.3779873847961426, 1.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.2207547426223755, 0.1985294073820114, 0.5, 0.1538461446762085, 1.7849056720733643, 0.5367646813392639, 0.5, 0.0, 2.3779873847961426, 1.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.2207547426223755, 0.1985294073820114, 0.5, 0.1538461446762085, 1.7776728868484497, 0.529411792755127, 0.5, 0.0, 2.3779873847961426, 1.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.2207547426223755, 0.1985294073820114, 0.5, 0.1538461446762085, 1.7704402208328247, 0.529411792755127, 0.5, 0.0, 2.3779873847961426, 1.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.2207547426223755, 0.1985294073820114, 0.5, 0.1538461446762085, 1.705345869064331, 0.529411792755127, 0.5, 0.0, 2.3779873847961426, 1.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.2207547426223755, 0.1985294073820114, 0.5, 0.1538461446762085, 1.6330188512802124, 0.6397058963775635, 0.5, 0.0, 2.3779873847961426, 1.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.2207547426223755, 0.1985294073820114, 0.5, 0.1538461446762085, 1.6257861852645874, 0.6764705777168274, 0.5, 0.0, 2.3779873847961426, 1.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.2207547426223755, 0.1985294073820114, 0.5, 0.1538461446762085, 1.6185534000396729, 0.7058823704719543, 0.5, 0.0, 2.3779873847961426, 1.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.2207547426223755, 0.1985294073820114, 0.5, 0.1538461446762085, 1.6185534000396729, 0.7132353186607361, 0.5, 0.0, 2.3779873847961426, 1.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.2207547426223755, 0.1985294073820114, 0.5, 0.1538461446762085, 1.6185534000396729, 0.7205882668495178, 0.5, 0.0, 2.3779873847961426, 1.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.2207547426223755, 0.1985294073820114, 0.5, 0.1538461446762085, 1.6185534000396729, 0.7132353186607361, 0.5, 0.0, 2.3779873847961426, 1.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.2207547426223755, 0.1985294073820114, 0.5, 0.1538461446762085, 1.6330188512802124, 0.6838235259056091, 0.5, 0.0, 2.3779873847961426, 1.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.2207547426223755, 0.1985294073820114, 0.5, 0.1538461446762085, 1.712578535079956, 0.5, 0.5, 0.0, 2.3779873847961426, 1.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.2207547426223755, 0.1985294073820114, 0.5, 0.1538461446762085, 1.7198113203048706, 0.49264705181121826, 0.5, 0.0, 2.3779873847961426, 1.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.2207547426223755, 0.1985294073820114, 0.5, 0.1538461446762085, 1.7559747695922852, 0.49264705181121826, 0.5, 0.0, 2.3779873847961426, 1.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.2207547426223755, 0.1985294073820114, 0.5, 0.1538461446762085, 1.7993710041046143, 0.5, 0.5, 0.0, 2.3779873847961426, 1.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.2207547426223755, 0.1985294073820114, 0.5, 0.1538461446762085, 1.8210691213607788, 0.5, 0.5, 0.0, 2.3779873847961426, 1.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.2207547426223755, 0.1985294073820114, 0.5, 0.1538461446762085, 1.8283019065856934, 0.5, 0.5, 0.0, 2.3779873847961426, 1.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# Properties modified on sample_0_rhoPWF
sample_0_rhoPWF.Points = [0.7, 0.0, 0.5, 0.0, 1.2207547426223755, 0.1985294073820114, 0.5, 0.1538461446762085, 1.857232689857483, 0.5, 0.5, 0.0, 2.3779873847961426, 1.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# hide data in view
Hide(rm_cuda_0hdf5_3, renderView1)

# set active source
SetActiveSource(richtmeyermeshkov_samples_mean_0hdf5)

# set active source
SetActiveSource(richtmeyermeshkov_samples_variance_0hdf5_2)

# set active source
SetActiveSource(richtmeyermeshkov_samples_mean_0hdf5)

# destroy richtmeyermeshkov_samples_mean_0hdf5
Delete(richtmeyermeshkov_samples_mean_0hdf5)
del richtmeyermeshkov_samples_mean_0hdf5

# set active source
SetActiveSource(richtmeyermeshkov_samples_mean_0hdf5_1)

# set active source
SetActiveSource(rm_cuda_0hdf5_3)

# destroy rm_cuda_0hdf5_3
Delete(rm_cuda_0hdf5_3)
del rm_cuda_0hdf5_3

# set active source
SetActiveSource(richtmeyermeshkov_samples_mean_0hdf5_1)

# destroy richtmeyermeshkov_samples_mean_0hdf5_1
Delete(richtmeyermeshkov_samples_mean_0hdf5_1)
del richtmeyermeshkov_samples_mean_0hdf5_1

# set active source
SetActiveSource(richtmeyermeshkov_samples_mean_0hdf5_2)

# destroy richtmeyermeshkov_samples_mean_0hdf5_2
Delete(richtmeyermeshkov_samples_mean_0hdf5_2)
del richtmeyermeshkov_samples_mean_0hdf5_2

# set active source
SetActiveSource(richtmeyermeshkov_samples_variance_0hdf5)

# destroy richtmeyermeshkov_samples_variance_0hdf5
Delete(richtmeyermeshkov_samples_variance_0hdf5)
del richtmeyermeshkov_samples_variance_0hdf5

# set active source
SetActiveSource(richtmeyermeshkov_samples_mean_0hdf5_3)

# destroy richtmeyermeshkov_samples_mean_0hdf5_3
Delete(richtmeyermeshkov_samples_mean_0hdf5_3)
del richtmeyermeshkov_samples_mean_0hdf5_3

# set active source
SetActiveSource(richtmeyermeshkov_samples_variance_0hdf5_1)

# destroy richtmeyermeshkov_samples_variance_0hdf5_1
Delete(richtmeyermeshkov_samples_variance_0hdf5_1)
del richtmeyermeshkov_samples_variance_0hdf5_1

# set active source
SetActiveSource(richtmeyermeshkov_samples_variance_0hdf5_2)

# destroy richtmeyermeshkov_samples_variance_0hdf5_2
Delete(richtmeyermeshkov_samples_variance_0hdf5_2)
del richtmeyermeshkov_samples_variance_0hdf5_2

# set active source
SetActiveSource(richtmeyermeshkov_samples_variance_0hdf5_3)

# destroy richtmeyermeshkov_samples_variance_0hdf5_3
Delete(richtmeyermeshkov_samples_variance_0hdf5_3)
del richtmeyermeshkov_samples_variance_0hdf5_3

# set active source
SetActiveSource(rm_cuda_0hdf5)

# destroy rm_cuda_0hdf5
Delete(rm_cuda_0hdf5)
del rm_cuda_0hdf5

# set active source
SetActiveSource(rm_cuda_0hdf5_1)

# destroy rm_cuda_0hdf5_1
Delete(rm_cuda_0hdf5_1)
del rm_cuda_0hdf5_1

# set active source
SetActiveSource(rm_cuda_0hdf5_2)

# destroy rm_cuda_0hdf5_2
Delete(rm_cuda_0hdf5_2)
del rm_cuda_0hdf5_2

# create a new 'NetCDF POP reader'
fbm_1nc = NetCDFPOPreader(FileName=['/scratch/snx3000/klye/fbm/single/H0_5/N512/fbm_1.nc'])

# show data in view
fbm_1ncDisplay = Show(fbm_1nc, renderView1)

# trace defaults for the display properties.
fbm_1ncDisplay.Representation = 'Outline'
fbm_1ncDisplay.ColorArrayName = ['POINTS', '']
fbm_1ncDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
fbm_1ncDisplay.SelectOrientationVectors = 'None'
fbm_1ncDisplay.ScaleFactor = -2.0000000000000002e+298
fbm_1ncDisplay.SelectScaleArray = 'None'
fbm_1ncDisplay.GlyphType = 'Arrow'
fbm_1ncDisplay.GlyphTableIndexArray = 'None'
fbm_1ncDisplay.GaussianRadius = -1e+297
fbm_1ncDisplay.SetScaleArray = [None, '']
fbm_1ncDisplay.ScaleTransferFunction = 'PiecewiseFunction'
fbm_1ncDisplay.OpacityArray = [None, '']
fbm_1ncDisplay.OpacityTransferFunction = 'PiecewiseFunction'
fbm_1ncDisplay.DataAxesGrid = 'GridAxesRepresentation'
fbm_1ncDisplay.SelectionCellLabelFontFile = ''
fbm_1ncDisplay.SelectionPointLabelFontFile = ''
fbm_1ncDisplay.PolarAxes = 'PolarAxesRepresentation'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
fbm_1ncDisplay.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1ncDisplay.DataAxesGrid.XTitleFontFile = ''
fbm_1ncDisplay.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1ncDisplay.DataAxesGrid.YTitleFontFile = ''
fbm_1ncDisplay.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1ncDisplay.DataAxesGrid.ZTitleFontFile = ''
fbm_1ncDisplay.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1ncDisplay.DataAxesGrid.XLabelFontFile = ''
fbm_1ncDisplay.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1ncDisplay.DataAxesGrid.YLabelFontFile = ''
fbm_1ncDisplay.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1ncDisplay.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
fbm_1ncDisplay.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1ncDisplay.PolarAxes.PolarAxisTitleFontFile = ''
fbm_1ncDisplay.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1ncDisplay.PolarAxes.PolarAxisLabelFontFile = ''
fbm_1ncDisplay.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1ncDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
fbm_1ncDisplay.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
fbm_1ncDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# destroy fbm_1nc
Delete(fbm_1nc)
del fbm_1nc

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-2.649111064298492, -5.282791339348038, 3.1398942537523786]
renderView1.CameraViewUp = [0.5259849499038038, 0.22390838089205406, 0.8204906272718732]
renderView1.CameraParallelScale = 1.7320508075688772

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).