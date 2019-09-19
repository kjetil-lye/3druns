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
kh_0hdf5 = NetCDFReader(FileName=['/scratch/snx3000/klye/3druns_new/kelvinhelmholtz_3d_tube/single/p0_1/N64/kh_0.hdf5'])
kh_0hdf5.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# show data in view
kh_0hdf5Display = Show(kh_0hdf5, renderView1)

# trace defaults for the display properties.
kh_0hdf5Display.Representation = 'Outline'
kh_0hdf5Display.ColorArrayName = [None, '']
kh_0hdf5Display.OSPRayScaleArray = 'sample_0_E'
kh_0hdf5Display.OSPRayScaleFunction = 'PiecewiseFunction'
kh_0hdf5Display.SelectOrientationVectors = 'None'
kh_0hdf5Display.ScaleFactor = 6.300000000000001
kh_0hdf5Display.SelectScaleArray = 'None'
kh_0hdf5Display.GlyphType = 'Arrow'
kh_0hdf5Display.GlyphTableIndexArray = 'None'
kh_0hdf5Display.GaussianRadius = 0.315
kh_0hdf5Display.SetScaleArray = ['POINTS', 'sample_0_E']
kh_0hdf5Display.ScaleTransferFunction = 'PiecewiseFunction'
kh_0hdf5Display.OpacityArray = ['POINTS', 'sample_0_E']
kh_0hdf5Display.OpacityTransferFunction = 'PiecewiseFunction'
kh_0hdf5Display.DataAxesGrid = 'GridAxesRepresentation'
kh_0hdf5Display.SelectionCellLabelFontFile = ''
kh_0hdf5Display.SelectionPointLabelFontFile = ''
kh_0hdf5Display.PolarAxes = 'PolarAxesRepresentation'
kh_0hdf5Display.ScalarOpacityUnitDistance = 1.7320508075688774
kh_0hdf5Display.Slice = 31

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
kh_0hdf5Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5Display.DataAxesGrid.XTitleFontFile = ''
kh_0hdf5Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5Display.DataAxesGrid.YTitleFontFile = ''
kh_0hdf5Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5Display.DataAxesGrid.ZTitleFontFile = ''
kh_0hdf5Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5Display.DataAxesGrid.XLabelFontFile = ''
kh_0hdf5Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5Display.DataAxesGrid.YLabelFontFile = ''
kh_0hdf5Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
kh_0hdf5Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5Display.PolarAxes.PolarAxisTitleFontFile = ''
kh_0hdf5Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5Display.PolarAxes.PolarAxisLabelFontFile = ''
kh_0hdf5Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5Display.PolarAxes.LastRadialAxisTextFontFile = ''
kh_0hdf5Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(kh_0hdf5Display, ('POINTS', 'sample_0_rho'))

# rescale color and/or opacity maps used to include current data range
kh_0hdf5Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
kh_0hdf5Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'sample_0_rho'
sample_0_rhoLUT = GetColorTransferFunction('sample_0_rho')
sample_0_rhoLUT.RGBPoints = [1.0, 0.231373, 0.298039, 0.752941, 1.5, 0.865003, 0.865003, 0.865003, 2.0, 0.705882, 0.0156863, 0.14902]
sample_0_rhoLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'sample_0_rho'
sample_0_rhoPWF = GetOpacityTransferFunction('sample_0_rho')
sample_0_rhoPWF.Points = [1.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]
sample_0_rhoPWF.ScalarRangeInitialized = 1

# change representation type
kh_0hdf5Display.SetRepresentationType('Volume')

# get color legend/bar for sample_0_rhoLUT in view renderView1
sample_0_rhoLUTColorBar = GetScalarBar(sample_0_rhoLUT, renderView1)
sample_0_rhoLUTColorBar.Title = 'sample_0_rho'
sample_0_rhoLUTColorBar.ComponentTitle = ''
sample_0_rhoLUTColorBar.HorizontalTitle = 1
sample_0_rhoLUTColorBar.TitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
sample_0_rhoLUTColorBar.TitleFontFile = ''
sample_0_rhoLUTColorBar.LabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
sample_0_rhoLUTColorBar.LabelFontFile = ''
sample_0_rhoLUTColorBar.RangeLabelFormat = '%-#6.1f'

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
sample_0_rhoLUT.ApplyPreset('Viridis (matplotlib)', True)

# Properties modified on sample_0_rhoLUTColorBar
sample_0_rhoLUTColorBar.Title = '\\varrho'

# Properties modified on sample_0_rhoLUTColorBar
sample_0_rhoLUTColorBar.Title = '$\\varrho$'

# current camera placement for renderView1
renderView1.CameraPosition = [144.40575502985845, 177.93974956477308, 133.8078326159454]
renderView1.CameraFocalPoint = [44.53092735830799, 26.747134810907053, 26.089027353401484]
renderView1.CameraViewUp = [-0.36689879607953924, 0.6882582503585181, -0.6258481079693509]
renderView1.CameraParallelScale = 54.559600438419636

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/kh/single/kh_64_fixed_0.png', renderView1, ImageResolution=[1216, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
kh_0hdf5_1 = NetCDFReader(FileName=['/scratch/snx3000/klye/3druns_new/kelvinhelmholtz_3d_tube/single/p0_1/N128/kh_0.hdf5'])
kh_0hdf5_1.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(kh_0hdf5, renderView1)

# set active source
SetActiveSource(kh_0hdf5)

# destroy kh_0hdf5
Delete(kh_0hdf5)
del kh_0hdf5

# set active source
SetActiveSource(kh_0hdf5_1)

# show data in view
kh_0hdf5_1Display = Show(kh_0hdf5_1, renderView1)

# trace defaults for the display properties.
kh_0hdf5_1Display.Representation = 'Outline'
kh_0hdf5_1Display.ColorArrayName = [None, '']
kh_0hdf5_1Display.OSPRayScaleArray = 'sample_0_E'
kh_0hdf5_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
kh_0hdf5_1Display.SelectOrientationVectors = 'None'
kh_0hdf5_1Display.ScaleFactor = 12.700000000000001
kh_0hdf5_1Display.SelectScaleArray = 'None'
kh_0hdf5_1Display.GlyphType = 'Arrow'
kh_0hdf5_1Display.GlyphTableIndexArray = 'None'
kh_0hdf5_1Display.GaussianRadius = 0.635
kh_0hdf5_1Display.SetScaleArray = ['POINTS', 'sample_0_E']
kh_0hdf5_1Display.ScaleTransferFunction = 'PiecewiseFunction'
kh_0hdf5_1Display.OpacityArray = ['POINTS', 'sample_0_E']
kh_0hdf5_1Display.OpacityTransferFunction = 'PiecewiseFunction'
kh_0hdf5_1Display.DataAxesGrid = 'GridAxesRepresentation'
kh_0hdf5_1Display.SelectionCellLabelFontFile = ''
kh_0hdf5_1Display.SelectionPointLabelFontFile = ''
kh_0hdf5_1Display.PolarAxes = 'PolarAxesRepresentation'
kh_0hdf5_1Display.ScalarOpacityUnitDistance = 1.732050807568877
kh_0hdf5_1Display.Slice = 63

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
kh_0hdf5_1Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5_1Display.DataAxesGrid.XTitleFontFile = ''
kh_0hdf5_1Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5_1Display.DataAxesGrid.YTitleFontFile = ''
kh_0hdf5_1Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5_1Display.DataAxesGrid.ZTitleFontFile = ''
kh_0hdf5_1Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5_1Display.DataAxesGrid.XLabelFontFile = ''
kh_0hdf5_1Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5_1Display.DataAxesGrid.YLabelFontFile = ''
kh_0hdf5_1Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5_1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
kh_0hdf5_1Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5_1Display.PolarAxes.PolarAxisTitleFontFile = ''
kh_0hdf5_1Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5_1Display.PolarAxes.PolarAxisLabelFontFile = ''
kh_0hdf5_1Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5_1Display.PolarAxes.LastRadialAxisTextFontFile = ''
kh_0hdf5_1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5_1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(kh_0hdf5_1Display, ('POINTS', 'sample_0_rho'))

# rescale color and/or opacity maps used to include current data range
kh_0hdf5_1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
kh_0hdf5_1Display.SetScalarBarVisibility(renderView1, True)

# change representation type
kh_0hdf5_1Display.SetRepresentationType('Volume')

# current camera placement for renderView1
renderView1.CameraPosition = [264.834970068046, 368.2851122816026, 280.64743283084226]
renderView1.CameraFocalPoint = [63.5, 63.5, 63.5]
renderView1.CameraViewUp = [-0.36689879607953924, 0.6882582503585181, -0.6258481079693509]
renderView1.CameraParallelScale = 109.9852262806237

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/kh/single/kh_128_fixed_0.png', renderView1, ImageResolution=[1216, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
kh_0hdf5 = NetCDFReader(FileName=['/scratch/snx3000/klye/3druns_new/kelvinhelmholtz_3d_tube/single/p0_1/N256/kh_0.hdf5'])
kh_0hdf5.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# set active source
SetActiveSource(kh_0hdf5_1)

# set active source
SetActiveSource(kh_0hdf5)

# show data in view
kh_0hdf5Display = Show(kh_0hdf5, renderView1)

# trace defaults for the display properties.
kh_0hdf5Display.Representation = 'Outline'
kh_0hdf5Display.ColorArrayName = [None, '']
kh_0hdf5Display.OSPRayScaleArray = 'sample_0_E'
kh_0hdf5Display.OSPRayScaleFunction = 'PiecewiseFunction'
kh_0hdf5Display.SelectOrientationVectors = 'None'
kh_0hdf5Display.ScaleFactor = 25.5
kh_0hdf5Display.SelectScaleArray = 'None'
kh_0hdf5Display.GlyphType = 'Arrow'
kh_0hdf5Display.GlyphTableIndexArray = 'None'
kh_0hdf5Display.GaussianRadius = 1.2750000000000001
kh_0hdf5Display.SetScaleArray = ['POINTS', 'sample_0_E']
kh_0hdf5Display.ScaleTransferFunction = 'PiecewiseFunction'
kh_0hdf5Display.OpacityArray = ['POINTS', 'sample_0_E']
kh_0hdf5Display.OpacityTransferFunction = 'PiecewiseFunction'
kh_0hdf5Display.DataAxesGrid = 'GridAxesRepresentation'
kh_0hdf5Display.SelectionCellLabelFontFile = ''
kh_0hdf5Display.SelectionPointLabelFontFile = ''
kh_0hdf5Display.PolarAxes = 'PolarAxesRepresentation'
kh_0hdf5Display.ScalarOpacityUnitDistance = 1.7320508075688774
kh_0hdf5Display.Slice = 127

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
kh_0hdf5Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5Display.DataAxesGrid.XTitleFontFile = ''
kh_0hdf5Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5Display.DataAxesGrid.YTitleFontFile = ''
kh_0hdf5Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5Display.DataAxesGrid.ZTitleFontFile = ''
kh_0hdf5Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5Display.DataAxesGrid.XLabelFontFile = ''
kh_0hdf5Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5Display.DataAxesGrid.YLabelFontFile = ''
kh_0hdf5Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
kh_0hdf5Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5Display.PolarAxes.PolarAxisTitleFontFile = ''
kh_0hdf5Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5Display.PolarAxes.PolarAxisLabelFontFile = ''
kh_0hdf5Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5Display.PolarAxes.LastRadialAxisTextFontFile = ''
kh_0hdf5Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# update the view to ensure updated data information
renderView1.Update()

# hide data in view
Hide(kh_0hdf5_1, renderView1)

# set scalar coloring
ColorBy(kh_0hdf5Display, ('POINTS', 'sample_0_rho'))

# rescale color and/or opacity maps used to include current data range
kh_0hdf5Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
kh_0hdf5Display.SetScalarBarVisibility(renderView1, True)

# change representation type
kh_0hdf5Display.SetRepresentationType('Volume')

# current camera placement for renderView1
renderView1.CameraPosition = [495.0793888995484, 716.8339561414372, 528.9748071364204]
renderView1.CameraFocalPoint = [63.5, 63.5, 63.5]
renderView1.CameraViewUp = [-0.36689879607953924, 0.6882582503585181, -0.6258481079693509]
renderView1.CameraParallelScale = 109.9852262806237

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/kh/single/kh_256_fixed_0.png', renderView1, ImageResolution=[1216, 799], 
    # PNG options
    CompressionLevel='0')

# set active source
SetActiveSource(kh_0hdf5_1)

# destroy kh_0hdf5_1
Delete(kh_0hdf5_1)
del kh_0hdf5_1

# set active source
SetActiveSource(kh_0hdf5)

# create a new 'NetCDF Reader'
kh_0hdf5_1 = NetCDFReader(FileName=['/scratch/snx3000/klye/3druns_new/kelvinhelmholtz_3d_tube/single/p0_1/N512/kh_0.hdf5'])
kh_0hdf5_1.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# show data in view
kh_0hdf5_1Display = Show(kh_0hdf5_1, renderView1)

# trace defaults for the display properties.
kh_0hdf5_1Display.Representation = 'Outline'
kh_0hdf5_1Display.ColorArrayName = [None, '']
kh_0hdf5_1Display.OSPRayScaleArray = 'sample_0_E'
kh_0hdf5_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
kh_0hdf5_1Display.SelectOrientationVectors = 'None'
kh_0hdf5_1Display.ScaleFactor = 51.1
kh_0hdf5_1Display.SelectScaleArray = 'None'
kh_0hdf5_1Display.GlyphType = 'Arrow'
kh_0hdf5_1Display.GlyphTableIndexArray = 'None'
kh_0hdf5_1Display.GaussianRadius = 2.555
kh_0hdf5_1Display.SetScaleArray = ['POINTS', 'sample_0_E']
kh_0hdf5_1Display.ScaleTransferFunction = 'PiecewiseFunction'
kh_0hdf5_1Display.OpacityArray = ['POINTS', 'sample_0_E']
kh_0hdf5_1Display.OpacityTransferFunction = 'PiecewiseFunction'
kh_0hdf5_1Display.DataAxesGrid = 'GridAxesRepresentation'
kh_0hdf5_1Display.SelectionCellLabelFontFile = ''
kh_0hdf5_1Display.SelectionPointLabelFontFile = ''
kh_0hdf5_1Display.PolarAxes = 'PolarAxesRepresentation'
kh_0hdf5_1Display.ScalarOpacityUnitDistance = 1.732050807568877
kh_0hdf5_1Display.Slice = 255

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
kh_0hdf5_1Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5_1Display.DataAxesGrid.XTitleFontFile = ''
kh_0hdf5_1Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5_1Display.DataAxesGrid.YTitleFontFile = ''
kh_0hdf5_1Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5_1Display.DataAxesGrid.ZTitleFontFile = ''
kh_0hdf5_1Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5_1Display.DataAxesGrid.XLabelFontFile = ''
kh_0hdf5_1Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5_1Display.DataAxesGrid.YLabelFontFile = ''
kh_0hdf5_1Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5_1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
kh_0hdf5_1Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5_1Display.PolarAxes.PolarAxisTitleFontFile = ''
kh_0hdf5_1Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5_1Display.PolarAxes.PolarAxisLabelFontFile = ''
kh_0hdf5_1Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5_1Display.PolarAxes.LastRadialAxisTextFontFile = ''
kh_0hdf5_1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5_1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(kh_0hdf5_1Display, ('POINTS', 'sample_0_rho'))

# rescale color and/or opacity maps used to include current data range
kh_0hdf5_1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
kh_0hdf5_1Display.SetScalarBarVisibility(renderView1, True)

# change representation type
kh_0hdf5_1Display.SetRepresentationType('Volume')

# hide data in view
Hide(kh_0hdf5, renderView1)

# current camera placement for renderView1
renderView1.CameraPosition = [988.6287486717107, 1463.9793575778165, 1061.2865879145393]
renderView1.CameraFocalPoint = [63.5, 63.5, 63.5]
renderView1.CameraViewUp = [-0.36689879607953924, 0.6882582503585181, -0.6258481079693509]
renderView1.CameraParallelScale = 109.9852262806237

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/kh/single/kh_512_fixed_0.png', renderView1, ImageResolution=[1216, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
kh_0hdf5_2 = NetCDFReader(FileName=['/scratch/snx3000/klye/3druns_new/kelvinhelmholtz_3d_tube/single/p0_1/N1024/kh_0.hdf5'])
kh_0hdf5_2.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# show data in view
kh_0hdf5_2Display = Show(kh_0hdf5_2, renderView1)

# trace defaults for the display properties.
kh_0hdf5_2Display.Representation = 'Outline'
kh_0hdf5_2Display.ColorArrayName = [None, '']
kh_0hdf5_2Display.OSPRayScaleArray = 'sample_0_E'
kh_0hdf5_2Display.OSPRayScaleFunction = 'PiecewiseFunction'
kh_0hdf5_2Display.SelectOrientationVectors = 'None'
kh_0hdf5_2Display.ScaleFactor = 102.30000000000001
kh_0hdf5_2Display.SelectScaleArray = 'None'
kh_0hdf5_2Display.GlyphType = 'Arrow'
kh_0hdf5_2Display.GlyphTableIndexArray = 'None'
kh_0hdf5_2Display.GaussianRadius = 5.115
kh_0hdf5_2Display.SetScaleArray = ['POINTS', 'sample_0_E']
kh_0hdf5_2Display.ScaleTransferFunction = 'PiecewiseFunction'
kh_0hdf5_2Display.OpacityArray = ['POINTS', 'sample_0_E']
kh_0hdf5_2Display.OpacityTransferFunction = 'PiecewiseFunction'
kh_0hdf5_2Display.DataAxesGrid = 'GridAxesRepresentation'
kh_0hdf5_2Display.SelectionCellLabelFontFile = ''
kh_0hdf5_2Display.SelectionPointLabelFontFile = ''
kh_0hdf5_2Display.PolarAxes = 'PolarAxesRepresentation'
kh_0hdf5_2Display.ScalarOpacityUnitDistance = 1.7320508075688772
kh_0hdf5_2Display.Slice = 511

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
kh_0hdf5_2Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5_2Display.DataAxesGrid.XTitleFontFile = ''
kh_0hdf5_2Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5_2Display.DataAxesGrid.YTitleFontFile = ''
kh_0hdf5_2Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5_2Display.DataAxesGrid.ZTitleFontFile = ''
kh_0hdf5_2Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5_2Display.DataAxesGrid.XLabelFontFile = ''
kh_0hdf5_2Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5_2Display.DataAxesGrid.YLabelFontFile = ''
kh_0hdf5_2Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5_2Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
kh_0hdf5_2Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5_2Display.PolarAxes.PolarAxisTitleFontFile = ''
kh_0hdf5_2Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5_2Display.PolarAxes.PolarAxisLabelFontFile = ''
kh_0hdf5_2Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5_2Display.PolarAxes.LastRadialAxisTextFontFile = ''
kh_0hdf5_2Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_0hdf5_2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(kh_0hdf5_2Display, ('POINTS', 'sample_0_rho'))

# rescale color and/or opacity maps used to include current data range
kh_0hdf5_2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
kh_0hdf5_2Display.SetScalarBarVisibility(renderView1, True)

# change representation type
kh_0hdf5_2Display.SetRepresentationType('Volume')

# current camera placement for renderView1
renderView1.CameraPosition = [1702.422011125605, 2544.534611189915, 1831.1398054724696]
renderView1.CameraFocalPoint = [63.5, 63.5, 63.5]
renderView1.CameraViewUp = [-0.36689879607953924, 0.6882582503585181, -0.6258481079693509]
renderView1.CameraParallelScale = 109.9852262806237

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/kh/single/kh_1024_fixed_0.png', renderView1, ImageResolution=[1216, 799], 
    # PNG options
    CompressionLevel='0')

# destroy kh_0hdf5_2
Delete(kh_0hdf5_2)
del kh_0hdf5_2

# set active source
SetActiveSource(kh_0hdf5_1)

# destroy kh_0hdf5_1
Delete(kh_0hdf5_1)
del kh_0hdf5_1

# set active source
SetActiveSource(kh_0hdf5)

# destroy kh_0hdf5
Delete(kh_0hdf5)
del kh_0hdf5

# create a new 'NetCDF Reader'
kh_1hdf5 = NetCDFReader(FileName=['/scratch/snx3000/klye/3druns_new/kelvinhelmholtz_3d_tube/single/p0_1/N1024/kh_1.hdf5'])
kh_1hdf5.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# show data in view
kh_1hdf5Display = Show(kh_1hdf5, renderView1)

# trace defaults for the display properties.
kh_1hdf5Display.Representation = 'Outline'
kh_1hdf5Display.ColorArrayName = [None, '']
kh_1hdf5Display.OSPRayScaleArray = 'sample_0_E'
kh_1hdf5Display.OSPRayScaleFunction = 'PiecewiseFunction'
kh_1hdf5Display.SelectOrientationVectors = 'None'
kh_1hdf5Display.ScaleFactor = 102.30000000000001
kh_1hdf5Display.SelectScaleArray = 'None'
kh_1hdf5Display.GlyphType = 'Arrow'
kh_1hdf5Display.GlyphTableIndexArray = 'None'
kh_1hdf5Display.GaussianRadius = 5.115
kh_1hdf5Display.SetScaleArray = ['POINTS', 'sample_0_E']
kh_1hdf5Display.ScaleTransferFunction = 'PiecewiseFunction'
kh_1hdf5Display.OpacityArray = ['POINTS', 'sample_0_E']
kh_1hdf5Display.OpacityTransferFunction = 'PiecewiseFunction'
kh_1hdf5Display.DataAxesGrid = 'GridAxesRepresentation'
kh_1hdf5Display.SelectionCellLabelFontFile = ''
kh_1hdf5Display.SelectionPointLabelFontFile = ''
kh_1hdf5Display.PolarAxes = 'PolarAxesRepresentation'
kh_1hdf5Display.ScalarOpacityUnitDistance = 1.7320508075688772
kh_1hdf5Display.Slice = 511

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
kh_1hdf5Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5Display.DataAxesGrid.XTitleFontFile = ''
kh_1hdf5Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5Display.DataAxesGrid.YTitleFontFile = ''
kh_1hdf5Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5Display.DataAxesGrid.ZTitleFontFile = ''
kh_1hdf5Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5Display.DataAxesGrid.XLabelFontFile = ''
kh_1hdf5Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5Display.DataAxesGrid.YLabelFontFile = ''
kh_1hdf5Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
kh_1hdf5Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5Display.PolarAxes.PolarAxisTitleFontFile = ''
kh_1hdf5Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5Display.PolarAxes.PolarAxisLabelFontFile = ''
kh_1hdf5Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5Display.PolarAxes.LastRadialAxisTextFontFile = ''
kh_1hdf5Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(kh_1hdf5Display, ('POINTS', 'sample_0_rho'))

# rescale color and/or opacity maps used to include current data range
kh_1hdf5Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
kh_1hdf5Display.SetScalarBarVisibility(renderView1, True)

# change representation type
kh_1hdf5Display.SetRepresentationType('Volume')

# rescale color and/or opacity maps used to exactly fit the current data range
kh_1hdf5Display.RescaleTransferFunctionToDataRange(False, True)

# Rescale transfer function
sample_0_rhoLUT.RescaleTransferFunction(1.1, 2.08989667892)

# Rescale transfer function
sample_0_rhoPWF.RescaleTransferFunction(1.1, 2.08989667892)

# Rescale transfer function
sample_0_rhoLUT.RescaleTransferFunction(1.2, 2.08989667892)

# Rescale transfer function
sample_0_rhoPWF.RescaleTransferFunction(1.2, 2.08989667892)

# Rescale transfer function
sample_0_rhoLUT.RescaleTransferFunction(1.05, 2.08989667892)

# Rescale transfer function
sample_0_rhoPWF.RescaleTransferFunction(1.05, 2.08989667892)

# current camera placement for renderView1
renderView1.CameraPosition = [2797.0084868519375, 2738.6629248928903, 1749.7626786320673]
renderView1.CameraFocalPoint = [511.5, 511.5, 511.5]
renderView1.CameraViewUp = [-0.35177090846720677, 0.7040035250868107, -0.6169572632050785]
renderView1.CameraParallelScale = 885.9439880714807

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/kh/single/kh_1024_fixed_1.png', renderView1, ImageResolution=[1216, 799], 
    # PNG options
    CompressionLevel='0')

# hide data in view
Hide(kh_1hdf5, renderView1)

# create a new 'NetCDF Reader'
kh_1hdf5_1 = NetCDFReader(FileName=['/scratch/snx3000/klye/3druns_new/kelvinhelmholtz_3d_tube/single/p0_1/N512/kh_1.hdf5'])
kh_1hdf5_1.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# show data in view
kh_1hdf5_1Display = Show(kh_1hdf5_1, renderView1)

# trace defaults for the display properties.
kh_1hdf5_1Display.Representation = 'Outline'
kh_1hdf5_1Display.ColorArrayName = [None, '']
kh_1hdf5_1Display.OSPRayScaleArray = 'sample_0_E'
kh_1hdf5_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
kh_1hdf5_1Display.SelectOrientationVectors = 'None'
kh_1hdf5_1Display.ScaleFactor = 51.1
kh_1hdf5_1Display.SelectScaleArray = 'None'
kh_1hdf5_1Display.GlyphType = 'Arrow'
kh_1hdf5_1Display.GlyphTableIndexArray = 'None'
kh_1hdf5_1Display.GaussianRadius = 2.555
kh_1hdf5_1Display.SetScaleArray = ['POINTS', 'sample_0_E']
kh_1hdf5_1Display.ScaleTransferFunction = 'PiecewiseFunction'
kh_1hdf5_1Display.OpacityArray = ['POINTS', 'sample_0_E']
kh_1hdf5_1Display.OpacityTransferFunction = 'PiecewiseFunction'
kh_1hdf5_1Display.DataAxesGrid = 'GridAxesRepresentation'
kh_1hdf5_1Display.SelectionCellLabelFontFile = ''
kh_1hdf5_1Display.SelectionPointLabelFontFile = ''
kh_1hdf5_1Display.PolarAxes = 'PolarAxesRepresentation'
kh_1hdf5_1Display.ScalarOpacityUnitDistance = 1.732050807568877
kh_1hdf5_1Display.Slice = 255

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
kh_1hdf5_1Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5_1Display.DataAxesGrid.XTitleFontFile = ''
kh_1hdf5_1Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5_1Display.DataAxesGrid.YTitleFontFile = ''
kh_1hdf5_1Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5_1Display.DataAxesGrid.ZTitleFontFile = ''
kh_1hdf5_1Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5_1Display.DataAxesGrid.XLabelFontFile = ''
kh_1hdf5_1Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5_1Display.DataAxesGrid.YLabelFontFile = ''
kh_1hdf5_1Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5_1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
kh_1hdf5_1Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5_1Display.PolarAxes.PolarAxisTitleFontFile = ''
kh_1hdf5_1Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5_1Display.PolarAxes.PolarAxisLabelFontFile = ''
kh_1hdf5_1Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5_1Display.PolarAxes.LastRadialAxisTextFontFile = ''
kh_1hdf5_1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5_1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(kh_1hdf5_1Display, ('POINTS', 'sample_0_rho'))

# rescale color and/or opacity maps used to include current data range
kh_1hdf5_1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
kh_1hdf5_1Display.SetScalarBarVisibility(renderView1, True)

# change representation type
kh_1hdf5_1Display.SetRepresentationType('Volume')

# current camera placement for renderView1
renderView1.CameraPosition = [1397.137181604438, 1367.9929175173675, 874.0261278406513]
renderView1.CameraFocalPoint = [255.5, 255.5, 255.5]
renderView1.CameraViewUp = [-0.35177090846720677, 0.7040035250868107, -0.6169572632050785]
renderView1.CameraParallelScale = 442.53898133384814

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/kh/single/kh_512_fixed_1.png', renderView1, ImageResolution=[1216, 799], 
    # PNG options
    CompressionLevel='0')

# hide data in view
Hide(kh_1hdf5_1, renderView1)

# create a new 'NetCDF Reader'
kh_1hdf5_2 = NetCDFReader(FileName=['/scratch/snx3000/klye/3druns_new/kelvinhelmholtz_3d_tube/single/p0_1/N256/kh_1.hdf5'])
kh_1hdf5_2.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# set active source
SetActiveSource(kh_1hdf5_1)

# set active source
SetActiveSource(kh_1hdf5_2)

# show data in view
kh_1hdf5_2Display = Show(kh_1hdf5_2, renderView1)

# trace defaults for the display properties.
kh_1hdf5_2Display.Representation = 'Outline'
kh_1hdf5_2Display.ColorArrayName = [None, '']
kh_1hdf5_2Display.OSPRayScaleArray = 'sample_0_E'
kh_1hdf5_2Display.OSPRayScaleFunction = 'PiecewiseFunction'
kh_1hdf5_2Display.SelectOrientationVectors = 'None'
kh_1hdf5_2Display.ScaleFactor = 25.5
kh_1hdf5_2Display.SelectScaleArray = 'None'
kh_1hdf5_2Display.GlyphType = 'Arrow'
kh_1hdf5_2Display.GlyphTableIndexArray = 'None'
kh_1hdf5_2Display.GaussianRadius = 1.2750000000000001
kh_1hdf5_2Display.SetScaleArray = ['POINTS', 'sample_0_E']
kh_1hdf5_2Display.ScaleTransferFunction = 'PiecewiseFunction'
kh_1hdf5_2Display.OpacityArray = ['POINTS', 'sample_0_E']
kh_1hdf5_2Display.OpacityTransferFunction = 'PiecewiseFunction'
kh_1hdf5_2Display.DataAxesGrid = 'GridAxesRepresentation'
kh_1hdf5_2Display.SelectionCellLabelFontFile = ''
kh_1hdf5_2Display.SelectionPointLabelFontFile = ''
kh_1hdf5_2Display.PolarAxes = 'PolarAxesRepresentation'
kh_1hdf5_2Display.ScalarOpacityUnitDistance = 1.7320508075688774
kh_1hdf5_2Display.Slice = 127

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
kh_1hdf5_2Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5_2Display.DataAxesGrid.XTitleFontFile = ''
kh_1hdf5_2Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5_2Display.DataAxesGrid.YTitleFontFile = ''
kh_1hdf5_2Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5_2Display.DataAxesGrid.ZTitleFontFile = ''
kh_1hdf5_2Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5_2Display.DataAxesGrid.XLabelFontFile = ''
kh_1hdf5_2Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5_2Display.DataAxesGrid.YLabelFontFile = ''
kh_1hdf5_2Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5_2Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
kh_1hdf5_2Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5_2Display.PolarAxes.PolarAxisTitleFontFile = ''
kh_1hdf5_2Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5_2Display.PolarAxes.PolarAxisLabelFontFile = ''
kh_1hdf5_2Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5_2Display.PolarAxes.LastRadialAxisTextFontFile = ''
kh_1hdf5_2Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5_2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(kh_1hdf5_2Display, ('POINTS', 'sample_0_rho'))

# rescale color and/or opacity maps used to include current data range
kh_1hdf5_2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
kh_1hdf5_2Display.SetScalarBarVisibility(renderView1, True)

# change representation type
kh_1hdf5_2Display.SetRepresentationType('Volume')

# current camera placement for renderView1
renderView1.CameraPosition = [697.2015289806883, 682.6579138296062, 436.15785244494344]
renderView1.CameraFocalPoint = [127.5, 127.5, 127.5]
renderView1.CameraViewUp = [-0.35177090846720677, 0.7040035250868107, -0.6169572632050785]
renderView1.CameraParallelScale = 220.83647796503186

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/kh/single/kh_256_fixed_1.png', renderView1, ImageResolution=[1063, 799], 
    # PNG options
    CompressionLevel='0')

# hide data in view
Hide(kh_1hdf5_2, renderView1)

# create a new 'NetCDF Reader'
kh_1hdf5_3 = NetCDFReader(FileName=['/scratch/snx3000/klye/3druns_new/kelvinhelmholtz_3d_tube/single/p0_1/N128/kh_1.hdf5'])
kh_1hdf5_3.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# show data in view
kh_1hdf5_3Display = Show(kh_1hdf5_3, renderView1)

# trace defaults for the display properties.
kh_1hdf5_3Display.Representation = 'Outline'
kh_1hdf5_3Display.ColorArrayName = [None, '']
kh_1hdf5_3Display.OSPRayScaleArray = 'sample_0_E'
kh_1hdf5_3Display.OSPRayScaleFunction = 'PiecewiseFunction'
kh_1hdf5_3Display.SelectOrientationVectors = 'None'
kh_1hdf5_3Display.ScaleFactor = 12.700000000000001
kh_1hdf5_3Display.SelectScaleArray = 'None'
kh_1hdf5_3Display.GlyphType = 'Arrow'
kh_1hdf5_3Display.GlyphTableIndexArray = 'None'
kh_1hdf5_3Display.GaussianRadius = 0.635
kh_1hdf5_3Display.SetScaleArray = ['POINTS', 'sample_0_E']
kh_1hdf5_3Display.ScaleTransferFunction = 'PiecewiseFunction'
kh_1hdf5_3Display.OpacityArray = ['POINTS', 'sample_0_E']
kh_1hdf5_3Display.OpacityTransferFunction = 'PiecewiseFunction'
kh_1hdf5_3Display.DataAxesGrid = 'GridAxesRepresentation'
kh_1hdf5_3Display.SelectionCellLabelFontFile = ''
kh_1hdf5_3Display.SelectionPointLabelFontFile = ''
kh_1hdf5_3Display.PolarAxes = 'PolarAxesRepresentation'
kh_1hdf5_3Display.ScalarOpacityUnitDistance = 1.732050807568877
kh_1hdf5_3Display.Slice = 63

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
kh_1hdf5_3Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5_3Display.DataAxesGrid.XTitleFontFile = ''
kh_1hdf5_3Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5_3Display.DataAxesGrid.YTitleFontFile = ''
kh_1hdf5_3Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5_3Display.DataAxesGrid.ZTitleFontFile = ''
kh_1hdf5_3Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5_3Display.DataAxesGrid.XLabelFontFile = ''
kh_1hdf5_3Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5_3Display.DataAxesGrid.YLabelFontFile = ''
kh_1hdf5_3Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5_3Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
kh_1hdf5_3Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5_3Display.PolarAxes.PolarAxisTitleFontFile = ''
kh_1hdf5_3Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5_3Display.PolarAxes.PolarAxisLabelFontFile = ''
kh_1hdf5_3Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5_3Display.PolarAxes.LastRadialAxisTextFontFile = ''
kh_1hdf5_3Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5_3Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(kh_1hdf5_3Display, ('POINTS', 'sample_0_rho'))

# rescale color and/or opacity maps used to include current data range
kh_1hdf5_3Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
kh_1hdf5_3Display.SetScalarBarVisibility(renderView1, True)

# change representation type
kh_1hdf5_3Display.SetRepresentationType('Volume')

# current camera placement for renderView1
renderView1.CameraPosition = [347.23370266881335, 339.99041198572536, 217.22371474708945]
renderView1.CameraFocalPoint = [63.5, 63.5, 63.5]
renderView1.CameraViewUp = [-0.35177090846720677, 0.7040035250868107, -0.6169572632050785]
renderView1.CameraParallelScale = 109.9852262806237

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/kh/single/kh_128_fixed_1.png', renderView1, ImageResolution=[1063, 799], 
    # PNG options
    CompressionLevel='0')

# hide data in view
Hide(kh_1hdf5_3, renderView1)

# create a new 'NetCDF Reader'
kh_1hdf5_4 = NetCDFReader(FileName=['/scratch/snx3000/klye/3druns_new/kelvinhelmholtz_3d_tube/single/p0_1/N64/kh_1.hdf5'])
kh_1hdf5_4.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# show data in view
kh_1hdf5_4Display = Show(kh_1hdf5_4, renderView1)

# trace defaults for the display properties.
kh_1hdf5_4Display.Representation = 'Outline'
kh_1hdf5_4Display.ColorArrayName = [None, '']
kh_1hdf5_4Display.OSPRayScaleArray = 'sample_0_E'
kh_1hdf5_4Display.OSPRayScaleFunction = 'PiecewiseFunction'
kh_1hdf5_4Display.SelectOrientationVectors = 'None'
kh_1hdf5_4Display.ScaleFactor = 6.300000000000001
kh_1hdf5_4Display.SelectScaleArray = 'None'
kh_1hdf5_4Display.GlyphType = 'Arrow'
kh_1hdf5_4Display.GlyphTableIndexArray = 'None'
kh_1hdf5_4Display.GaussianRadius = 0.315
kh_1hdf5_4Display.SetScaleArray = ['POINTS', 'sample_0_E']
kh_1hdf5_4Display.ScaleTransferFunction = 'PiecewiseFunction'
kh_1hdf5_4Display.OpacityArray = ['POINTS', 'sample_0_E']
kh_1hdf5_4Display.OpacityTransferFunction = 'PiecewiseFunction'
kh_1hdf5_4Display.DataAxesGrid = 'GridAxesRepresentation'
kh_1hdf5_4Display.SelectionCellLabelFontFile = ''
kh_1hdf5_4Display.SelectionPointLabelFontFile = ''
kh_1hdf5_4Display.PolarAxes = 'PolarAxesRepresentation'
kh_1hdf5_4Display.ScalarOpacityUnitDistance = 1.7320508075688774
kh_1hdf5_4Display.Slice = 31

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
kh_1hdf5_4Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5_4Display.DataAxesGrid.XTitleFontFile = ''
kh_1hdf5_4Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5_4Display.DataAxesGrid.YTitleFontFile = ''
kh_1hdf5_4Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5_4Display.DataAxesGrid.ZTitleFontFile = ''
kh_1hdf5_4Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5_4Display.DataAxesGrid.XLabelFontFile = ''
kh_1hdf5_4Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5_4Display.DataAxesGrid.YLabelFontFile = ''
kh_1hdf5_4Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5_4Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
kh_1hdf5_4Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5_4Display.PolarAxes.PolarAxisTitleFontFile = ''
kh_1hdf5_4Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5_4Display.PolarAxes.PolarAxisLabelFontFile = ''
kh_1hdf5_4Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5_4Display.PolarAxes.LastRadialAxisTextFontFile = ''
kh_1hdf5_4Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_1hdf5_4Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(kh_1hdf5_4Display, ('POINTS', 'sample_0_rho'))

# rescale color and/or opacity maps used to include current data range
kh_1hdf5_4Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
kh_1hdf5_4Display.SetScalarBarVisibility(renderView1, True)

# change representation type
kh_1hdf5_4Display.SetRepresentationType('Volume')

# current camera placement for renderView1
renderView1.CameraPosition = [172.24978951287596, 168.65666106378504, 107.7566458981625]
renderView1.CameraFocalPoint = [31.5, 31.5, 31.5]
renderView1.CameraViewUp = [-0.35177090846720677, 0.7040035250868107, -0.6169572632050785]
renderView1.CameraParallelScale = 54.559600438419636

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/kh/single/kh_64_fixed_1.png', renderView1, ImageResolution=[1063, 799], 
    # PNG options
    CompressionLevel='0')

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [172.24978951287596, 168.65666106378504, 107.7566458981625]
renderView1.CameraFocalPoint = [31.5, 31.5, 31.5]
renderView1.CameraViewUp = [-0.35177090846720677, 0.7040035250868107, -0.6169572632050785]
renderView1.CameraParallelScale = 54.559600438419636

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).