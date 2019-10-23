# trace generated using paraview version 5.6.2
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'NetCDF Reader'
kh_1hdf5 = NetCDFReader(FileName=['/scratch/snx3000/klye/3druns_new/kelvinhelmholtz_3d_tube/single/p0_01/N1024/kh_1.hdf5'])
kh_1hdf5.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1107, 799]

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

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(kh_1hdf5Display, ('POINTS', 'sample_0_rho'))

# rescale color and/or opacity maps used to include current data range
kh_1hdf5Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
kh_1hdf5Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'sample_0_rho'
sample_0_rhoLUT = GetColorTransferFunction('sample_0_rho')
sample_0_rhoLUT.RGBPoints = [0.9745140671730042, 0.267004, 0.004874, 0.329415, 0.9942240230015519, 0.26851, 0.009605, 0.335427, 1.0139289533441669, 0.269944, 0.014625, 0.341379, 1.033638909172713, 0.271305, 0.019942, 0.347269, 1.053343839515328, 0.272594, 0.025563, 0.353093, 1.0730537953438761, 0.273809, 0.031497, 0.358853, 1.0927587256864908, 0.274952, 0.037752, 0.364543, 1.1124686815150377, 0.276022, 0.044167, 0.370164, 1.1321786373435858, 0.277018, 0.050344, 0.375715, 1.1518835676861998, 0.277941, 0.056324, 0.381191, 1.1715935235147477, 0.278791, 0.062145, 0.386592, 1.1912984538573625, 0.279566, 0.067836, 0.391917, 1.2110084096859106, 0.280267, 0.073417, 0.397163, 1.2307133400285246, 0.280894, 0.078907, 0.402329, 1.2504232958570718, 0.281446, 0.08432, 0.407414, 1.2701332516856194, 0.281924, 0.089666, 0.412415, 1.2898381820282345, 0.282327, 0.094955, 0.417331, 1.3095481378567806, 0.282656, 0.100196, 0.42216, 1.329253068199396, 0.28291, 0.105393, 0.426902, 1.3489630240279435, 0.283091, 0.110553, 0.431554, 1.3686679543705584, 0.283197, 0.11568, 0.436115, 1.3883779101991065, 0.283229, 0.120777, 0.440584, 1.4080878660276532, 0.283187, 0.125848, 0.44496, 1.4277927963702675, 0.283072, 0.130895, 0.449241, 1.4475027521988155, 0.282884, 0.13592, 0.453427, 1.4672076825414302, 0.282623, 0.140926, 0.457517, 1.4869176383699774, 0.28229, 0.145912, 0.46151, 1.5066225687125923, 0.281887, 0.150881, 0.465405, 1.5263325245411394, 0.281412, 0.155834, 0.469201, 1.5460374548837548, 0.280868, 0.160771, 0.472899, 1.565747410712302, 0.280255, 0.165693, 0.476498, 1.585457366540849, 0.279574, 0.170599, 0.479997, 1.6051622968834638, 0.278826, 0.17549, 0.483397, 1.6248722527120112, 0.278012, 0.180367, 0.486697, 1.6445771830546259, 0.277134, 0.185228, 0.489898, 1.6642871388831737, 0.276194, 0.190074, 0.493001, 1.6839920692257877, 0.275191, 0.194905, 0.496005, 1.7037020250543349, 0.274128, 0.199721, 0.498911, 1.723411980882883, 0.273006, 0.20452, 0.501721, 1.7431169112254978, 0.271828, 0.209303, 0.504434, 1.7628268670540455, 0.270595, 0.214069, 0.507052, 1.7825317973966588, 0.269308, 0.218818, 0.509577, 1.8022417532252069, 0.267968, 0.223549, 0.512008, 1.8219466835678229, 0.26658, 0.228262, 0.514349, 1.8416566393963698, 0.265145, 0.232956, 0.516599, 1.8613665952249177, 0.263663, 0.237631, 0.518762, 1.8810715255675312, 0.262138, 0.242286, 0.520837, 1.9007814813960793, 0.260571, 0.246922, 0.522828, 1.9204864117386946, 0.258965, 0.251537, 0.524736, 1.9401963675672418, 0.257322, 0.25613, 0.526563, 1.9599012979098558, 0.255645, 0.260703, 0.528312, 1.9796112537384036, 0.253935, 0.265254, 0.529983, 1.9993212095669517, 0.252194, 0.269783, 0.531579, 2.019026139909567, 0.250425, 0.27429, 0.533103, 2.0387360957381127, 0.248629, 0.278775, 0.534556, 2.058441026080728, 0.246811, 0.283237, 0.535941, 2.0781509819092747, 0.244972, 0.287675, 0.53726, 2.097855912251891, 0.243113, 0.292092, 0.538516, 2.1175658680804377, 0.241237, 0.296485, 0.539709, 2.1372758239089853, 0.239346, 0.300855, 0.540844, 2.156980754251599, 0.237441, 0.305202, 0.541921, 2.1766907100801465, 0.235526, 0.309527, 0.542944, 2.196395640422762, 0.233603, 0.313828, 0.543914, 2.2161055962513085, 0.231674, 0.318106, 0.544834, 2.235810526593922, 0.229739, 0.322361, 0.545706, 2.255520482422471, 0.227802, 0.326594, 0.546532, 2.275230438251018, 0.225863, 0.330805, 0.547314, 2.2949353685936345, 0.223925, 0.334994, 0.548053, 2.3146453244221803, 0.221989, 0.339161, 0.548752, 2.3343502547647956, 0.220057, 0.343307, 0.549413, 2.3540602105933432, 0.21813, 0.347432, 0.550038, 2.3737651409359577, 0.21621, 0.351535, 0.550627, 2.3934750967645053, 0.214298, 0.355619, 0.551184, 2.413185052593052, 0.212395, 0.359683, 0.55171, 2.432889982935665, 0.210503, 0.363727, 0.552206, 2.4525999387642146, 0.208623, 0.367752, 0.552675, 2.4723048691068295, 0.206756, 0.371758, 0.553117, 2.4920148249353766, 0.204903, 0.375746, 0.553533, 2.5117197552779915, 0.203063, 0.379716, 0.553925, 2.531429711106539, 0.201239, 0.38367, 0.554294, 2.5511346414491545, 0.19943, 0.387607, 0.554642, 2.570844597277702, 0.197636, 0.391528, 0.554969, 2.5905545531062497, 0.19586, 0.395433, 0.555276, 2.6102594834488624, 0.1941, 0.399323, 0.555565, 2.6299694392774104, 0.192357, 0.403199, 0.555836, 2.649674369620025, 0.190631, 0.407061, 0.556089, 2.6693843254485725, 0.188923, 0.41091, 0.556326, 2.6890892557911883, 0.187231, 0.414746, 0.556547, 2.7087992116197324, 0.185556, 0.41857, 0.556753, 2.7285091674482813, 0.183898, 0.422383, 0.556944, 2.7482140977908975, 0.182256, 0.426184, 0.55712, 2.7679240536194443, 0.180629, 0.429975, 0.557282, 2.7876289839620583, 0.179019, 0.433756, 0.55743, 2.8073389397906063, 0.177423, 0.437527, 0.557565, 2.8270438701332212, 0.175841, 0.44129, 0.557685, 2.8467538259617693, 0.174274, 0.445044, 0.557792, 2.8664637817903156, 0.172719, 0.448791, 0.557885, 2.886168712132932, 0.171176, 0.45253, 0.557965, 2.9058786679614776, 0.169646, 0.456262, 0.55803, 2.925583598304092, 0.168126, 0.459988, 0.558082, 2.94529355413264, 0.166617, 0.463708, 0.558119, 2.964998484475255, 0.165117, 0.467423, 0.558141, 2.984708440303803, 0.163625, 0.471133, 0.558148, 3.0044183961323503, 0.162142, 0.474838, 0.55814, 3.0241233264749643, 0.160665, 0.47854, 0.558115, 3.043833282303511, 0.159194, 0.482237, 0.558073, 3.0635382126461295, 0.157729, 0.485932, 0.558013, 3.083248168474675, 0.15627, 0.489624, 0.557936, 3.102953098817289, 0.154815, 0.493313, 0.55784, 3.122663054645836, 0.153364, 0.497, 0.557724, 3.142373010474384, 0.151918, 0.500685, 0.557587, 3.1620779408169972, 0.150476, 0.504369, 0.55743, 3.1817878966455453, 0.149039, 0.508051, 0.55725, 3.20149282698816, 0.147607, 0.511733, 0.557049, 3.2212027828167074, 0.14618, 0.515413, 0.556823, 3.240907713159323, 0.144759, 0.519093, 0.556572, 3.2606176689878716, 0.143343, 0.522773, 0.556295, 3.2803276248164184, 0.141935, 0.526453, 0.555991, 3.3000325551590333, 0.140536, 0.530132, 0.555659, 3.319742510987579, 0.139147, 0.533812, 0.555298, 3.3394474413301927, 0.13777, 0.537492, 0.554906, 3.359157397158742, 0.136408, 0.541173, 0.554483, 3.378862327501357, 0.135066, 0.544853, 0.554029, 3.398572283329904, 0.133743, 0.548535, 0.553541, 3.4182822391584504, 0.132444, 0.552216, 0.553018, 3.437987169501067, 0.131172, 0.555899, 0.552459, 3.457697125329614, 0.129933, 0.559582, 0.551864, 3.4774020556722287, 0.128729, 0.563265, 0.551229, 3.4971120115007746, 0.127568, 0.566949, 0.550556, 3.516816941843391, 0.126453, 0.570633, 0.549841, 3.536526897671938, 0.125394, 0.574318, 0.549086, 3.5562318280145533, 0.124395, 0.578002, 0.548287, 3.5759417838431, 0.123463, 0.581687, 0.547445, 3.5956517396716463, 0.122606, 0.585371, 0.546557, 3.615356670014263, 0.121831, 0.589055, 0.545623, 3.6350666258428097, 0.121148, 0.592739, 0.544641, 3.6547715561854237, 0.120565, 0.596422, 0.543611, 3.674481512013971, 0.120092, 0.600104, 0.54253, 3.694186442356586, 0.119738, 0.603785, 0.5414, 3.7138963981851343, 0.119512, 0.607464, 0.540218, 3.7336063540136823, 0.119423, 0.611141, 0.538982, 3.7533112843562946, 0.119483, 0.614817, 0.537692, 3.7730212401848453, 0.119699, 0.61849, 0.536347, 3.7927261705274566, 0.120081, 0.622161, 0.534946, 3.812436126356007, 0.120638, 0.625828, 0.533488, 3.832141056698621, 0.12138, 0.629492, 0.531973, 3.851851012527167, 0.122312, 0.633153, 0.530398, 3.8715609683557126, 0.123444, 0.636809, 0.528763, 3.891265898698326, 0.12478, 0.640461, 0.527068, 3.910975854526877, 0.126326, 0.644107, 0.525311, 3.930680784869493, 0.128087, 0.647749, 0.523491, 3.950390740698042, 0.130067, 0.651384, 0.521608, 3.9700956710406548, 0.132268, 0.655014, 0.519661, 3.989805626869201, 0.134692, 0.658636, 0.517649, 4.009515582697749, 0.137339, 0.662252, 0.515571, 4.029220513040364, 0.14021, 0.665859, 0.513427, 4.04893046886891, 0.143303, 0.669459, 0.511215, 4.0686353992115265, 0.146616, 0.67305, 0.508936, 4.088345355040074, 0.150148, 0.676631, 0.506589, 4.108050285382689, 0.153894, 0.680203, 0.504172, 4.127760241211234, 0.157851, 0.683765, 0.501686, 4.147470197039783, 0.162016, 0.687316, 0.499129, 4.1671751273824, 0.166383, 0.690856, 0.496502, 4.186885083210944, 0.170948, 0.694384, 0.493803, 4.20659001355356, 0.175707, 0.6979, 0.491033, 4.226299969382107, 0.180653, 0.701402, 0.488189, 4.246004899724721, 0.185783, 0.704891, 0.485273, 4.265714855553268, 0.19109, 0.708366, 0.482284, 4.285424811381817, 0.196571, 0.711827, 0.479221, 4.305129741724433, 0.202219, 0.715272, 0.476084, 4.32483969755298, 0.20803, 0.718701, 0.472873, 4.344544627895591, 0.214, 0.722114, 0.469588, 4.364254583724141, 0.220124, 0.725509, 0.466226, 4.383959514066758, 0.226397, 0.728888, 0.462789, 4.403669469895305, 0.232815, 0.732247, 0.459277, 4.423379425723851, 0.239374, 0.735588, 0.455688, 4.443084356066462, 0.24607, 0.73891, 0.452024, 4.462794311895014, 0.252899, 0.742211, 0.448284, 4.482499242237628, 0.259857, 0.745492, 0.444467, 4.502209198066175, 0.266941, 0.748751, 0.440573, 4.521914128408791, 0.274149, 0.751988, 0.436601, 4.5416240842373385, 0.281477, 0.755203, 0.432552, 4.5613290145799485, 0.288921, 0.758394, 0.428426, 4.581038970408501, 0.296479, 0.761561, 0.424223, 4.600748926237047, 0.304148, 0.764704, 0.419943, 4.62045385657966, 0.311925, 0.767822, 0.415586, 4.6401638124082085, 0.319809, 0.770914, 0.411152, 4.659868742750825, 0.327796, 0.77398, 0.40664, 4.679578698579374, 0.335885, 0.777018, 0.402049, 4.699283628921986, 0.344074, 0.780029, 0.397381, 4.718993584750534, 0.35236, 0.783011, 0.392636, 4.738703540579081, 0.360741, 0.785964, 0.387814, 4.758408470921698, 0.369214, 0.788888, 0.382914, 4.778118426750242, 0.377779, 0.791781, 0.377939, 4.7978233570928595, 0.386433, 0.794644, 0.372886, 4.817533312921404, 0.395174, 0.797475, 0.367757, 4.837238243264019, 0.404001, 0.800275, 0.362552, 4.8569481990925665, 0.412913, 0.803041, 0.357269, 4.876658154921116, 0.421908, 0.805774, 0.35191, 4.896363085263729, 0.430983, 0.808473, 0.346476, 4.916073041092276, 0.440137, 0.811138, 0.340967, 4.935777971434892, 0.449368, 0.813768, 0.335384, 4.955487927263439, 0.458674, 0.816363, 0.329727, 4.975192857606053, 0.468053, 0.818921, 0.323998, 4.994902813434602, 0.477504, 0.821444, 0.318195, 5.01461276926315, 0.487026, 0.823929, 0.312321, 5.034317699605762, 0.496615, 0.826376, 0.306377, 5.054027655434306, 0.506271, 0.828786, 0.300362, 5.073732585776926, 0.515992, 0.831158, 0.294279, 5.093442541605474, 0.525776, 0.833491, 0.288127, 5.113147471948087, 0.535621, 0.835785, 0.281908, 5.132857427776634, 0.545524, 0.838039, 0.275626, 5.152567383605185, 0.555484, 0.840254, 0.269281, 5.172272313947797, 0.565498, 0.84243, 0.262877, 5.1919822697763465, 0.575563, 0.844566, 0.256415, 5.21168720011896, 0.585678, 0.846661, 0.249897, 5.231397155947504, 0.595839, 0.848717, 0.243329, 5.251102086290117, 0.606045, 0.850733, 0.236712, 5.27081204211867, 0.616293, 0.852709, 0.230052, 5.2905219979472164, 0.626579, 0.854645, 0.223353, 5.310226928289833, 0.636902, 0.856542, 0.21662, 5.3299368841183785, 0.647257, 0.8584, 0.209861, 5.34964181446099, 0.657642, 0.860219, 0.203082, 5.369351770289539, 0.668054, 0.861999, 0.196293, 5.389056700632157, 0.678489, 0.863742, 0.189503, 5.408766656460702, 0.688944, 0.865448, 0.182725, 5.42847661228925, 0.699415, 0.867117, 0.175971, 5.448181542631865, 0.709898, 0.868751, 0.169257, 5.467891498460411, 0.720391, 0.87035, 0.162603, 5.487596428803028, 0.730889, 0.871916, 0.156029, 5.507306384631572, 0.741388, 0.873449, 0.149561, 5.527011314974188, 0.751884, 0.874951, 0.143228, 5.546721270802736, 0.762373, 0.876424, 0.137064, 5.5664262011453545, 0.772852, 0.877868, 0.131109, 5.586136156973896, 0.783315, 0.879285, 0.125405, 5.605846112802446, 0.79376, 0.880678, 0.120005, 5.625551043145062, 0.804182, 0.882046, 0.114965, 5.64526099897361, 0.814576, 0.883393, 0.110347, 5.6649659293162244, 0.82494, 0.88472, 0.106217, 5.68467588514477, 0.83527, 0.886029, 0.102646, 5.704380815487385, 0.845561, 0.887322, 0.099702, 5.724090771315932, 0.85581, 0.888601, 0.097452, 5.743800727144484, 0.866013, 0.889868, 0.095953, 5.763505657487098, 0.876168, 0.891125, 0.09525, 5.783215613315644, 0.886271, 0.892374, 0.095374, 5.802920543658256, 0.89632, 0.893616, 0.096335, 5.822630499486804, 0.906311, 0.894855, 0.098125, 5.8423354298294194, 0.916242, 0.896091, 0.100717, 5.862045385657967, 0.926106, 0.89733, 0.104071, 5.8817553414865165, 0.935904, 0.89857, 0.108131, 5.90146027182913, 0.945636, 0.899815, 0.112838, 5.921170227657675, 0.9553, 0.901065, 0.118128, 5.940875158000291, 0.964894, 0.902323, 0.123941, 5.960585113828842, 0.974417, 0.90359, 0.130215, 5.980290044171453, 0.983868, 0.904867, 0.136897, 6.0, 0.993248, 0.906157, 0.143936]
sample_0_rhoLUT.NanColor = [1.0, 0.0, 0.0]
sample_0_rhoLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'sample_0_rho'
sample_0_rhoPWF = GetOpacityTransferFunction('sample_0_rho')
sample_0_rhoPWF.Points = [0.9745140671730042, 0.0, 0.5, 0.0, 6.0, 1.0, 0.5, 0.0]
sample_0_rhoPWF.ScalarRangeInitialized = 1

# change representation type
kh_1hdf5Display.SetRepresentationType('Volume')

# rescale color and/or opacity maps used to exactly fit the current data range
kh_1hdf5Display.RescaleTransferFunctionToDataRange(False, True)

# Rescale transfer function
sample_0_rhoLUT.RescaleTransferFunction(1.2, 2.06257653236)

# Rescale transfer function
sample_0_rhoPWF.RescaleTransferFunction(1.2, 2.06257653236)

# Rescale transfer function
sample_0_rhoLUT.RescaleTransferFunction(1.2, 2.1)

# Rescale transfer function
sample_0_rhoPWF.RescaleTransferFunction(1.2, 2.1)

# current camera placement for renderView1
renderView1.CameraPosition = [2180.538086877376, 2803.4137077983946, 2429.452454921987]
renderView1.CameraFocalPoint = [511.5, 511.5, 511.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 885.9439880714807

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/kh/single/p0_01/kh_single_1024_cm_0_1.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
kh_1hdf5_1 = NetCDFReader(FileName=['/scratch/snx3000/klye/3druns_new/kelvinhelmholtz_3d_tube/single/p0_01/N512/kh_1.hdf5'])
kh_1hdf5_1.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(kh_1hdf5, renderView1)

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

# Rescale transfer function
sample_0_rhoLUT.RescaleTransferFunction(1.2, 2.1)

# Rescale transfer function
sample_0_rhoPWF.RescaleTransferFunction(1.2, 2.1)

# current camera placement for renderView1
renderView1.CameraPosition = [1089.2032867979851, 1400.336661471143, 1213.538811793876]
renderView1.CameraFocalPoint = [255.5, 255.5, 255.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 442.53898133384814

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/kh/single/p0_01/kh_single_512_cm_0_1.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
kh_1hdf5_2 = NetCDFReader(FileName=['/scratch/snx3000/klye/3druns_new/kelvinhelmholtz_3d_tube/single/p0_01/N256/kh_1.hdf5'])
kh_1hdf5_2.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(kh_1hdf5_1, renderView1)

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

# Rescale transfer function
sample_0_rhoLUT.RescaleTransferFunction(1.2, 2.1)

# Rescale transfer function
sample_0_rhoPWF.RescaleTransferFunction(1.2, 2.1)

# current camera placement for renderView1
renderView1.CameraPosition = [543.5358867582902, 698.7981383075178, 605.5819902298208]
renderView1.CameraFocalPoint = [127.5, 127.5, 127.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 220.83647796503186

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/kh/single/p0_01/kh_single_256_cm_0_1.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
kh_1hdf5_3 = NetCDFReader(FileName=['/scratch/snx3000/klye/3druns_new/kelvinhelmholtz_3d_tube/single/p0_01/N128/kh_1.hdf5'])
kh_1hdf5_3.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(kh_1hdf5_2, renderView1)

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

# Rescale transfer function
sample_0_rhoLUT.RescaleTransferFunction(1.2, 2.1)

# Rescale transfer function
sample_0_rhoPWF.RescaleTransferFunction(1.2, 2.1)

# current camera placement for renderView1
renderView1.CameraPosition = [270.7021867384425, 348.0288767257049, 301.60357944779304]
renderView1.CameraFocalPoint = [63.5, 63.5, 63.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 109.9852262806237

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/kh/single/p0_01/kh_single_128_cm_0_1.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# set active source
SetActiveSource(kh_1hdf5)

# destroy kh_1hdf5
Delete(kh_1hdf5)
del kh_1hdf5

# set active source
SetActiveSource(kh_1hdf5_1)

# destroy kh_1hdf5_1
Delete(kh_1hdf5_1)
del kh_1hdf5_1

# set active source
SetActiveSource(kh_1hdf5_2)

# destroy kh_1hdf5_2
Delete(kh_1hdf5_2)
del kh_1hdf5_2

# create a new 'NetCDF Reader'
kh_1hdf5 = NetCDFReader(FileName=['/scratch/snx3000/klye/3druns_new/kelvinhelmholtz_3d_tube/single/p0_1/N512/kh_1.hdf5'])
kh_1hdf5.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(kh_1hdf5_3, renderView1)

# show data in view
kh_1hdf5Display = Show(kh_1hdf5, renderView1)

# trace defaults for the display properties.
kh_1hdf5Display.Representation = 'Outline'
kh_1hdf5Display.ColorArrayName = [None, '']
kh_1hdf5Display.OSPRayScaleArray = 'sample_0_E'
kh_1hdf5Display.OSPRayScaleFunction = 'PiecewiseFunction'
kh_1hdf5Display.SelectOrientationVectors = 'None'
kh_1hdf5Display.ScaleFactor = 51.1
kh_1hdf5Display.SelectScaleArray = 'None'
kh_1hdf5Display.GlyphType = 'Arrow'
kh_1hdf5Display.GlyphTableIndexArray = 'None'
kh_1hdf5Display.GaussianRadius = 2.555
kh_1hdf5Display.SetScaleArray = ['POINTS', 'sample_0_E']
kh_1hdf5Display.ScaleTransferFunction = 'PiecewiseFunction'
kh_1hdf5Display.OpacityArray = ['POINTS', 'sample_0_E']
kh_1hdf5Display.OpacityTransferFunction = 'PiecewiseFunction'
kh_1hdf5Display.DataAxesGrid = 'GridAxesRepresentation'
kh_1hdf5Display.SelectionCellLabelFontFile = ''
kh_1hdf5Display.SelectionPointLabelFontFile = ''
kh_1hdf5Display.PolarAxes = 'PolarAxesRepresentation'
kh_1hdf5Display.ScalarOpacityUnitDistance = 1.732050807568877
kh_1hdf5Display.Slice = 255

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

# Rescale transfer function
sample_0_rhoLUT.RescaleTransferFunction(1.2, 2.1)

# Rescale transfer function
sample_0_rhoPWF.RescaleTransferFunction(1.2, 2.1)

# current camera placement for renderView1
renderView1.CameraPosition = [1089.2032867979851, 1400.3366614711433, 1213.538811793876]
renderView1.CameraFocalPoint = [255.5, 255.5, 255.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 442.53898133384814

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/kh/single/p0_1/kh_single_512_cm_0_1.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
kh_1hdf5_1 = NetCDFReader(FileName=['/scratch/snx3000/klye/3druns_new/kelvinhelmholtz_3d_tube/single/p0_1/N1024/kh_1.hdf5'])
kh_1hdf5_1.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# show data in view
kh_1hdf5_1Display = Show(kh_1hdf5_1, renderView1)

# trace defaults for the display properties.
kh_1hdf5_1Display.Representation = 'Outline'
kh_1hdf5_1Display.ColorArrayName = [None, '']
kh_1hdf5_1Display.OSPRayScaleArray = 'sample_0_E'
kh_1hdf5_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
kh_1hdf5_1Display.SelectOrientationVectors = 'None'
kh_1hdf5_1Display.ScaleFactor = 102.30000000000001
kh_1hdf5_1Display.SelectScaleArray = 'None'
kh_1hdf5_1Display.GlyphType = 'Arrow'
kh_1hdf5_1Display.GlyphTableIndexArray = 'None'
kh_1hdf5_1Display.GaussianRadius = 5.115
kh_1hdf5_1Display.SetScaleArray = ['POINTS', 'sample_0_E']
kh_1hdf5_1Display.ScaleTransferFunction = 'PiecewiseFunction'
kh_1hdf5_1Display.OpacityArray = ['POINTS', 'sample_0_E']
kh_1hdf5_1Display.OpacityTransferFunction = 'PiecewiseFunction'
kh_1hdf5_1Display.DataAxesGrid = 'GridAxesRepresentation'
kh_1hdf5_1Display.SelectionCellLabelFontFile = ''
kh_1hdf5_1Display.SelectionPointLabelFontFile = ''
kh_1hdf5_1Display.PolarAxes = 'PolarAxesRepresentation'
kh_1hdf5_1Display.ScalarOpacityUnitDistance = 1.7320508075688772
kh_1hdf5_1Display.Slice = 511

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

# update the view to ensure updated data information
renderView1.Update()

# Rescale transfer function
sample_0_rhoLUT.RescaleTransferFunction(0.979507923126, 2.1)

# Rescale transfer function
sample_0_rhoPWF.RescaleTransferFunction(0.979507923126, 2.1)

# hide data in view
Hide(kh_1hdf5, renderView1)

# set active source
SetActiveSource(kh_1hdf5)

# show data in view
kh_1hdf5Display = Show(kh_1hdf5, renderView1)

# show color bar/color legend
kh_1hdf5Display.SetScalarBarVisibility(renderView1, True)

# Rescale transfer function
sample_0_rhoLUT.RescaleTransferFunction(1.2, 2.1)

# Rescale transfer function
sample_0_rhoPWF.RescaleTransferFunction(1.2, 2.1)

# hide data in view
Hide(kh_1hdf5, renderView1)

# hide data in view
Hide(kh_1hdf5_1, renderView1)

# set active source
SetActiveSource(kh_1hdf5_1)

# show data in view
kh_1hdf5_1Display = Show(kh_1hdf5_1, renderView1)

# reset view to fit data
renderView1.ResetCamera()

# set scalar coloring
ColorBy(kh_1hdf5_1Display, ('POINTS', 'sample_0_E'))

# rescale color and/or opacity maps used to include current data range
kh_1hdf5_1Display.RescaleTransferFunctionToDataRange(True, True)

# change representation type
kh_1hdf5_1Display.SetRepresentationType('Volume')

# get color transfer function/color map for 'sample_0_E'
sample_0_ELUT = GetColorTransferFunction('sample_0_E')
sample_0_ELUT.RGBPoints = [5.466089248657227, 0.231373, 0.298039, 0.752941, 6.148226976394653, 0.865003, 0.865003, 0.865003, 6.83036470413208, 0.705882, 0.0156863, 0.14902]
sample_0_ELUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'sample_0_E'
sample_0_EPWF = GetOpacityTransferFunction('sample_0_E')
sample_0_EPWF.Points = [5.466089248657227, 0.0, 0.5, 0.0, 6.83036470413208, 1.0, 0.5, 0.0]
sample_0_EPWF.ScalarRangeInitialized = 1

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
sample_0_ELUT.ApplyPreset('Viridis (matplotlib)', True)

# Rescale transfer function
sample_0_ELUT.RescaleTransferFunction(1.2, 2.1)

# Rescale transfer function
sample_0_EPWF.RescaleTransferFunction(1.2, 2.1)

# set scalar coloring
ColorBy(kh_1hdf5_1Display, ('POINTS', 'sample_0_rho'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(sample_0_ELUT, renderView1)

# rescale color and/or opacity maps used to include current data range
kh_1hdf5_1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
kh_1hdf5_1Display.SetScalarBarVisibility(renderView1, True)

# Rescale transfer function
sample_0_rhoLUT.RescaleTransferFunction(1.2, 2.1)

# Rescale transfer function
sample_0_rhoPWF.RescaleTransferFunction(1.2, 2.1)

# rescale color and/or opacity maps used to exactly fit the current data range
kh_1hdf5_1Display.RescaleTransferFunctionToDataRange(False, True)

# rescale color and/or opacity maps used to exactly fit the current data range
kh_1hdf5_1Display.RescaleTransferFunctionToDataRange(False, True)

# rescale color and/or opacity maps used to exactly fit the current data range
kh_1hdf5_1Display.RescaleTransferFunctionToDataRange(False, True)

# rescale color and/or opacity maps used to exactly fit the current data range
kh_1hdf5_1Display.RescaleTransferFunctionToDataRange(False, True)

# hide data in view
Hide(kh_1hdf5_1, renderView1)

# show data in view
kh_1hdf5_1Display = Show(kh_1hdf5_1, renderView1)

# show color bar/color legend
kh_1hdf5_1Display.SetScalarBarVisibility(renderView1, True)

# reset view to fit data
renderView1.ResetCamera()

# destroy kh_1hdf5_1
Delete(kh_1hdf5_1)
del kh_1hdf5_1

# create a new 'NetCDF Reader'
kh_1hdf5_1 = NetCDFReader(FileName=['/scratch/snx3000/klye/3druns_new/kelvinhelmholtz_3d_tube/single/p0_1/N1024/kh_1.hdf5'])
kh_1hdf5_1.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# show data in view
kh_1hdf5_1Display = Show(kh_1hdf5_1, renderView1)

# trace defaults for the display properties.
kh_1hdf5_1Display.Representation = 'Outline'
kh_1hdf5_1Display.ColorArrayName = [None, '']
kh_1hdf5_1Display.OSPRayScaleArray = 'sample_0_E'
kh_1hdf5_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
kh_1hdf5_1Display.SelectOrientationVectors = 'None'
kh_1hdf5_1Display.ScaleFactor = 102.30000000000001
kh_1hdf5_1Display.SelectScaleArray = 'None'
kh_1hdf5_1Display.GlyphType = 'Arrow'
kh_1hdf5_1Display.GlyphTableIndexArray = 'None'
kh_1hdf5_1Display.GaussianRadius = 5.115
kh_1hdf5_1Display.SetScaleArray = ['POINTS', 'sample_0_E']
kh_1hdf5_1Display.ScaleTransferFunction = 'PiecewiseFunction'
kh_1hdf5_1Display.OpacityArray = ['POINTS', 'sample_0_E']
kh_1hdf5_1Display.OpacityTransferFunction = 'PiecewiseFunction'
kh_1hdf5_1Display.DataAxesGrid = 'GridAxesRepresentation'
kh_1hdf5_1Display.SelectionCellLabelFontFile = ''
kh_1hdf5_1Display.SelectionPointLabelFontFile = ''
kh_1hdf5_1Display.PolarAxes = 'PolarAxesRepresentation'
kh_1hdf5_1Display.ScalarOpacityUnitDistance = 1.7320508075688772
kh_1hdf5_1Display.Slice = 511

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

# Rescale transfer function
sample_0_rhoLUT.RescaleTransferFunction(1.2, 2.1)

# Rescale transfer function
sample_0_rhoPWF.RescaleTransferFunction(1.2, 2.1)

# current camera placement for renderView1
renderView1.CameraPosition = [2180.5380868773755, 2803.4137077983946, 2429.452454921987]
renderView1.CameraFocalPoint = [511.5, 511.5, 511.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 885.9439880714807

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/kh/single/p0_1/kh_single_1024_cm_0_1.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# hide data in view
Hide(kh_1hdf5_1, renderView1)

# create a new 'NetCDF Reader'
kh_1hdf5_2 = NetCDFReader(FileName=['/scratch/snx3000/klye/3druns_new/kelvinhelmholtz_3d_tube/single/p0_1/N256/kh_1.hdf5'])
kh_1hdf5_2.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

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

# Rescale transfer function
sample_0_rhoLUT.RescaleTransferFunction(1.2, 2.1)

# Rescale transfer function
sample_0_rhoPWF.RescaleTransferFunction(1.2, 2.1)

# current camera placement for renderView1
renderView1.CameraPosition = [543.5358867582901, 698.7981383075178, 605.5819902298208]
renderView1.CameraFocalPoint = [127.5, 127.5, 127.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 220.83647796503186

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/kh/single/p0_1/kh_single_256_cm_0_1.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
kh_1hdf5_4 = NetCDFReader(FileName=['/scratch/snx3000/klye/3druns_new/kelvinhelmholtz_3d_tube/single/p0_1/N128/kh_1.hdf5'])
kh_1hdf5_4.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(kh_1hdf5_2, renderView1)

# show data in view
kh_1hdf5_4Display = Show(kh_1hdf5_4, renderView1)

# trace defaults for the display properties.
kh_1hdf5_4Display.Representation = 'Outline'
kh_1hdf5_4Display.ColorArrayName = [None, '']
kh_1hdf5_4Display.OSPRayScaleArray = 'sample_0_E'
kh_1hdf5_4Display.OSPRayScaleFunction = 'PiecewiseFunction'
kh_1hdf5_4Display.SelectOrientationVectors = 'None'
kh_1hdf5_4Display.ScaleFactor = 12.700000000000001
kh_1hdf5_4Display.SelectScaleArray = 'None'
kh_1hdf5_4Display.GlyphType = 'Arrow'
kh_1hdf5_4Display.GlyphTableIndexArray = 'None'
kh_1hdf5_4Display.GaussianRadius = 0.635
kh_1hdf5_4Display.SetScaleArray = ['POINTS', 'sample_0_E']
kh_1hdf5_4Display.ScaleTransferFunction = 'PiecewiseFunction'
kh_1hdf5_4Display.OpacityArray = ['POINTS', 'sample_0_E']
kh_1hdf5_4Display.OpacityTransferFunction = 'PiecewiseFunction'
kh_1hdf5_4Display.DataAxesGrid = 'GridAxesRepresentation'
kh_1hdf5_4Display.SelectionCellLabelFontFile = ''
kh_1hdf5_4Display.SelectionPointLabelFontFile = ''
kh_1hdf5_4Display.PolarAxes = 'PolarAxesRepresentation'
kh_1hdf5_4Display.ScalarOpacityUnitDistance = 1.732050807568877
kh_1hdf5_4Display.Slice = 63

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

# Rescale transfer function
sample_0_rhoLUT.RescaleTransferFunction(1.2, 2.1)

# Rescale transfer function
sample_0_rhoPWF.RescaleTransferFunction(1.2, 2.1)

# current camera placement for renderView1
renderView1.CameraPosition = [270.7021867384425, 348.0288767257049, 301.60357944779304]
renderView1.CameraFocalPoint = [63.5, 63.5, 63.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 109.9852262806237

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/kh/single/p0_1/kh_single_128_cm_0_1.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# hide data in view
Hide(kh_1hdf5_4, renderView1)

# create a new 'NetCDF Reader'
kh_mean_0hdf5 = NetCDFReader(FileName=['/scratch/snx3000/klye/3druns_new/kelvinhelmholtz_3d_tube/stats/p0_1/N512/kh_mean_0.hdf5'])
kh_mean_0hdf5.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# set active source
SetActiveSource(kh_1hdf5_3)

# destroy kh_1hdf5_3
Delete(kh_1hdf5_3)
del kh_1hdf5_3

# set active source
SetActiveSource(kh_1hdf5)

# destroy kh_1hdf5
Delete(kh_1hdf5)
del kh_1hdf5

# set active source
SetActiveSource(kh_1hdf5_1)

# destroy kh_1hdf5_1
Delete(kh_1hdf5_1)
del kh_1hdf5_1

# set active source
SetActiveSource(kh_1hdf5_2)

# destroy kh_1hdf5_2
Delete(kh_1hdf5_2)
del kh_1hdf5_2

# set active source
SetActiveSource(kh_1hdf5_4)

# destroy kh_1hdf5_4
Delete(kh_1hdf5_4)
del kh_1hdf5_4

# set active source
SetActiveSource(kh_mean_0hdf5)

# show data in view
kh_mean_0hdf5Display = Show(kh_mean_0hdf5, renderView1)

# trace defaults for the display properties.
kh_mean_0hdf5Display.Representation = 'Outline'
kh_mean_0hdf5Display.ColorArrayName = [None, '']
kh_mean_0hdf5Display.OSPRayScaleArray = 'E'
kh_mean_0hdf5Display.OSPRayScaleFunction = 'PiecewiseFunction'
kh_mean_0hdf5Display.SelectOrientationVectors = 'E'
kh_mean_0hdf5Display.ScaleFactor = 51.1
kh_mean_0hdf5Display.SelectScaleArray = 'E'
kh_mean_0hdf5Display.GlyphType = 'Arrow'
kh_mean_0hdf5Display.GlyphTableIndexArray = 'E'
kh_mean_0hdf5Display.GaussianRadius = 2.555
kh_mean_0hdf5Display.SetScaleArray = ['POINTS', 'E']
kh_mean_0hdf5Display.ScaleTransferFunction = 'PiecewiseFunction'
kh_mean_0hdf5Display.OpacityArray = ['POINTS', 'E']
kh_mean_0hdf5Display.OpacityTransferFunction = 'PiecewiseFunction'
kh_mean_0hdf5Display.DataAxesGrid = 'GridAxesRepresentation'
kh_mean_0hdf5Display.SelectionCellLabelFontFile = ''
kh_mean_0hdf5Display.SelectionPointLabelFontFile = ''
kh_mean_0hdf5Display.PolarAxes = 'PolarAxesRepresentation'
kh_mean_0hdf5Display.ScalarOpacityUnitDistance = 1.732050807568877
kh_mean_0hdf5Display.Slice = 255

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
kh_mean_0hdf5Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5Display.DataAxesGrid.XTitleFontFile = ''
kh_mean_0hdf5Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5Display.DataAxesGrid.YTitleFontFile = ''
kh_mean_0hdf5Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5Display.DataAxesGrid.ZTitleFontFile = ''
kh_mean_0hdf5Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5Display.DataAxesGrid.XLabelFontFile = ''
kh_mean_0hdf5Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5Display.DataAxesGrid.YLabelFontFile = ''
kh_mean_0hdf5Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
kh_mean_0hdf5Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5Display.PolarAxes.PolarAxisTitleFontFile = ''
kh_mean_0hdf5Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5Display.PolarAxes.PolarAxisLabelFontFile = ''
kh_mean_0hdf5Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5Display.PolarAxes.LastRadialAxisTextFontFile = ''
kh_mean_0hdf5Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(kh_mean_0hdf5Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
kh_mean_0hdf5Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
kh_mean_0hdf5Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'rho'
rhoLUT = GetColorTransferFunction('rho')
rhoLUT.RGBPoints = [0.05, 0.267004, 0.004874, 0.329415, 0.057698273569011596, 0.26851, 0.009605, 0.335427, 0.06539458429417423, 0.269944, 0.014625, 0.341379, 0.07309285786318746, 0.271305, 0.019942, 0.347269, 0.0807891685883539, 0.272594, 0.025563, 0.353093, 0.08848744215736168, 0.273809, 0.031497, 0.358853, 0.09618375288252815, 0.274952, 0.037752, 0.364543, 0.10388202645153974, 0.276022, 0.044167, 0.370164, 0.11158030002055105, 0.277018, 0.050344, 0.375715, 0.11927661074571559, 0.277941, 0.056324, 0.381191, 0.1269748843147291, 0.278791, 0.062145, 0.386592, 0.13467119503989367, 0.279566, 0.067836, 0.391917, 0.14236946860890332, 0.280267, 0.073417, 0.397163, 0.15006577933406762, 0.280894, 0.078907, 0.402329, 0.1577640529030811, 0.281446, 0.08432, 0.407414, 0.1654623264720908, 0.281924, 0.089666, 0.412415, 0.17315863719725533, 0.282327, 0.094955, 0.417331, 0.1808569107662688, 0.282656, 0.100196, 0.42216, 0.18855322149142928, 0.28291, 0.105393, 0.426902, 0.1962514950604447, 0.283091, 0.110553, 0.431554, 0.20394780578560923, 0.283197, 0.11568, 0.436115, 0.21164607935461893, 0.283229, 0.120777, 0.440584, 0.21934435292363025, 0.283187, 0.125848, 0.44496, 0.227040663648797, 0.283072, 0.130895, 0.449241, 0.23473893721780642, 0.282884, 0.13592, 0.453427, 0.24243524794297472, 0.282623, 0.140926, 0.457517, 0.2501335215119844, 0.28229, 0.145912, 0.46151, 0.25782983223714895, 0.281887, 0.150881, 0.465405, 0.2655281058061584, 0.281412, 0.155834, 0.469201, 0.2732244165313229, 0.280868, 0.160771, 0.472899, 0.2809226901003383, 0.280255, 0.165693, 0.476498, 0.28862096366934614, 0.279574, 0.170599, 0.479997, 0.29631727439451255, 0.278826, 0.17549, 0.483397, 0.30401554796352415, 0.278012, 0.180367, 0.486697, 0.31171185868868645, 0.277134, 0.185228, 0.489898, 0.3194101322577, 0.276194, 0.190074, 0.493001, 0.3271064429828645, 0.275191, 0.194905, 0.496005, 0.33480471655187805, 0.274128, 0.199721, 0.498911, 0.3425029901208877, 0.273006, 0.20452, 0.501721, 0.3501993008460523, 0.271828, 0.209303, 0.504434, 0.35789757441506576, 0.270595, 0.214069, 0.507052, 0.3655938851402281, 0.269308, 0.218818, 0.509577, 0.37329215870923943, 0.267968, 0.223549, 0.512008, 0.38098846943440623, 0.26658, 0.228262, 0.514349, 0.3886867430034178, 0.265145, 0.232956, 0.516599, 0.39638501657242914, 0.263663, 0.237631, 0.518762, 0.40408132729759366, 0.262138, 0.242286, 0.520837, 0.41177960086660526, 0.260571, 0.246922, 0.522828, 0.4194759115917717, 0.258965, 0.251537, 0.524736, 0.4271741851607792, 0.257322, 0.25613, 0.526563, 0.4348704958859457, 0.255645, 0.260703, 0.528312, 0.4425687694549553, 0.253935, 0.265254, 0.529983, 0.45026704302396886, 0.252194, 0.269783, 0.531579, 0.4579633537491315, 0.250425, 0.27429, 0.533103, 0.4656616273181428, 0.248629, 0.278775, 0.534556, 0.47335793804330734, 0.246811, 0.283237, 0.535941, 0.48105621161232087, 0.244972, 0.287675, 0.53726, 0.48875252233748345, 0.243113, 0.292092, 0.538516, 0.496450795906497, 0.241237, 0.296485, 0.539709, 0.5041490694755045, 0.239346, 0.300855, 0.540844, 0.5118453802006728, 0.237441, 0.305202, 0.541921, 0.5195436537696845, 0.235526, 0.309527, 0.542944, 0.527239964494849, 0.233603, 0.313828, 0.543914, 0.5349382380638622, 0.231674, 0.318106, 0.544834, 0.5426345487890227, 0.229739, 0.322361, 0.545706, 0.5503328223580365, 0.227802, 0.326594, 0.546532, 0.5580310959270476, 0.225863, 0.330805, 0.547314, 0.5657274066522121, 0.223925, 0.334994, 0.548053, 0.573425680221224, 0.221989, 0.339161, 0.548752, 0.5811219909463885, 0.220057, 0.343307, 0.549413, 0.5888202645153982, 0.21813, 0.347432, 0.550038, 0.5965165752405646, 0.21621, 0.351535, 0.550627, 0.6042148488095757, 0.214298, 0.355619, 0.551184, 0.6119131223785875, 0.212395, 0.359683, 0.55171, 0.619609433103752, 0.210503, 0.363727, 0.552206, 0.6273077066727636, 0.208623, 0.367752, 0.552675, 0.6350040173979263, 0.206756, 0.371758, 0.553117, 0.6427022909669393, 0.204903, 0.375746, 0.553533, 0.6503986016921038, 0.203063, 0.379716, 0.553925, 0.6580968752611135, 0.201239, 0.38367, 0.554294, 0.6657931859862802, 0.19943, 0.387607, 0.554642, 0.6734914595552918, 0.197636, 0.391528, 0.554969, 0.6811897331243029, 0.19586, 0.395433, 0.555276, 0.6888860438494674, 0.1941, 0.399323, 0.555565, 0.6965843174184811, 0.192357, 0.403199, 0.555836, 0.7042806281436417, 0.190631, 0.407061, 0.556089, 0.7119789017126554, 0.188923, 0.41091, 0.556326, 0.71967521243782, 0.187231, 0.414746, 0.556547, 0.7273734860068332, 0.185556, 0.41857, 0.556753, 0.7350717595758428, 0.183898, 0.422383, 0.556944, 0.7427680703010074, 0.182256, 0.426184, 0.55712, 0.7504663438700203, 0.180629, 0.429975, 0.557282, 0.7581626545951848, 0.179019, 0.433756, 0.55743, 0.7658609281641967, 0.177423, 0.437527, 0.557565, 0.7735572388893613, 0.175841, 0.44129, 0.557685, 0.781255512458373, 0.174274, 0.445044, 0.557792, 0.7889537860273826, 0.172719, 0.448791, 0.557885, 0.7966500967525494, 0.171176, 0.45253, 0.557965, 0.8043483703215604, 0.169646, 0.456262, 0.55803, 0.8120446810467249, 0.168126, 0.459988, 0.558082, 0.8197429546157368, 0.166617, 0.463708, 0.558119, 0.8274392653409011, 0.165117, 0.467423, 0.558141, 0.8351375389099109, 0.163625, 0.471133, 0.558148, 0.8428358124789239, 0.162142, 0.474838, 0.55814, 0.8505321232040884, 0.160665, 0.47854, 0.558115, 0.8582303967730982, 0.159194, 0.482237, 0.558073, 0.8659267074982646, 0.157729, 0.485932, 0.558013, 0.8736249810672757, 0.15627, 0.489624, 0.557936, 0.8813212917924402, 0.154815, 0.493313, 0.55784, 0.8890195653614521, 0.153364, 0.497, 0.557724, 0.8967178389304634, 0.151918, 0.500685, 0.557587, 0.9044141496556302, 0.150476, 0.504369, 0.55743, 0.9121124232246393, 0.149039, 0.508051, 0.55725, 0.9198087339498043, 0.147607, 0.511733, 0.557049, 0.9275070075188173, 0.14618, 0.515413, 0.556823, 0.9352033182439802, 0.144759, 0.519093, 0.556572, 0.9429015918129915, 0.143343, 0.522773, 0.556295, 0.9505998653820013, 0.141935, 0.526453, 0.555991, 0.9582961761071696, 0.140536, 0.530132, 0.555659, 0.9659944496761792, 0.139147, 0.533812, 0.555298, 0.9736907604013454, 0.13777, 0.537492, 0.554906, 0.9813890339703573, 0.136408, 0.541173, 0.554483, 0.9890853446955197, 0.135066, 0.544853, 0.554029, 0.9967836182645315, 0.133743, 0.548535, 0.553541, 1.0044818918335428, 0.132444, 0.552216, 0.553018, 1.012178202558709, 0.131172, 0.555899, 0.552459, 1.0198764761277208, 0.129933, 0.559582, 0.551864, 1.0275727868528848, 0.128729, 0.563265, 0.551229, 1.0352710604218947, 0.127568, 0.566949, 0.550556, 1.042967371147059, 0.126453, 0.570633, 0.549841, 1.0506656447160712, 0.125394, 0.574318, 0.549086, 1.0583619554412371, 0.124395, 0.578002, 0.548287, 1.066060229010249, 0.123463, 0.581687, 0.547445, 1.0737585025792604, 0.122606, 0.585371, 0.546557, 1.0814548133044228, 0.121831, 0.589055, 0.545623, 1.0891530868734347, 0.121148, 0.592739, 0.544641, 1.0968493975986007, 0.120565, 0.596422, 0.543611, 1.1045476711676103, 0.120092, 0.600104, 0.54253, 1.112243981892779, 0.119738, 0.603785, 0.5414, 1.1199422554617886, 0.119512, 0.607464, 0.540218, 1.1276405290307983, 0.119423, 0.611141, 0.538982, 1.1353368397559642, 0.119483, 0.614817, 0.537692, 1.143035113324976, 0.119699, 0.61849, 0.536347, 1.1507314240501407, 0.120081, 0.622161, 0.534946, 1.15842969761915, 0.120638, 0.625828, 0.533488, 1.1661260083443146, 0.12138, 0.629492, 0.531973, 1.173824281913328, 0.122312, 0.633153, 0.530398, 1.1815225554823399, 0.123444, 0.636809, 0.528763, 1.1892188662075038, 0.12478, 0.640461, 0.527068, 1.1969171397765195, 0.126326, 0.644107, 0.525311, 1.2046134505016826, 0.128087, 0.647749, 0.523491, 1.21231172407069, 0.130067, 0.651384, 0.521608, 1.220008034795856, 0.132268, 0.655014, 0.519661, 1.2277063083648674, 0.134692, 0.658636, 0.517649, 1.2354045819338815, 0.137339, 0.662252, 0.515571, 1.243100892659046, 0.14021, 0.665859, 0.513427, 1.250799166228055, 0.143303, 0.669459, 0.511215, 1.2584954769532217, 0.146616, 0.67305, 0.508936, 1.2661937505222312, 0.150148, 0.676631, 0.506589, 1.2738900612473956, 0.153894, 0.680203, 0.504172, 1.2815883348164052, 0.157851, 0.683765, 0.501686, 1.2892866083854204, 0.162016, 0.687316, 0.499129, 1.2969829191105835, 0.166383, 0.690856, 0.496502, 1.304681192679599, 0.170948, 0.694384, 0.493803, 1.3123775034047636, 0.175707, 0.6979, 0.491033, 1.3200757769737728, 0.180653, 0.701402, 0.488189, 1.3277720876989334, 0.185783, 0.704891, 0.485273, 1.3354703612679453, 0.19109, 0.708366, 0.482284, 1.3431686348369627, 0.196571, 0.711827, 0.479221, 1.3508649455621289, 0.202219, 0.715272, 0.476084, 1.3585632191311379, 0.20803, 0.718701, 0.472873, 1.3662595298563012, 0.214, 0.722114, 0.469588, 1.3739578034253108, 0.220124, 0.725509, 0.466226, 1.381654114150481, 0.226397, 0.728888, 0.462789, 1.3893523877194864, 0.232815, 0.732247, 0.459277, 1.397050661288496, 0.239374, 0.735588, 0.455688, 1.404746972013663, 0.24607, 0.73891, 0.452024, 1.4124452455826835, 0.252899, 0.742211, 0.448284, 1.4201415563078428, 0.259857, 0.745492, 0.444467, 1.4278398298768522, 0.266941, 0.748751, 0.440573, 1.4355361406020146, 0.274149, 0.751988, 0.436601, 1.4432344141710318, 0.281477, 0.755203, 0.432552, 1.4509307248961942, 0.288921, 0.758394, 0.428426, 1.4586289984652114, 0.296479, 0.761561, 0.424223, 1.466327272034218, 0.304148, 0.764704, 0.419943, 1.4740235827593804, 0.311925, 0.767822, 0.415586, 1.4817218563283931, 0.319809, 0.770914, 0.411152, 1.4894181670535525, 0.327796, 0.77398, 0.40664, 1.4971164406225699, 0.335885, 0.777018, 0.402049, 1.5048127513477323, 0.344074, 0.780029, 0.397381, 1.5125110249167462, 0.35236, 0.783011, 0.392636, 1.5202092984857556, 0.360741, 0.785964, 0.387814, 1.5279056092109218, 0.369214, 0.788888, 0.382914, 1.5356038827799359, 0.377779, 0.791781, 0.377939, 1.5433001935050938, 0.386433, 0.794644, 0.372886, 1.5509984670741035, 0.395174, 0.797475, 0.367757, 1.5586947777992735, 0.404001, 0.800275, 0.362552, 1.5663930513682833, 0.412913, 0.803041, 0.357269, 1.574091324937293, 0.421908, 0.805774, 0.35191, 1.581787635662464, 0.430983, 0.808473, 0.346476, 1.5894859092314726, 0.440137, 0.811138, 0.340967, 1.5971822199566392, 0.449368, 0.813768, 0.335384, 1.604880493525649, 0.458674, 0.816363, 0.329727, 1.6125768042508113, 0.468053, 0.818921, 0.323998, 1.620275077819821, 0.477504, 0.821444, 0.318195, 1.627973351388834, 0.487026, 0.823929, 0.312321, 1.6356696621140008, 0.496615, 0.826376, 0.306377, 1.6433679356830104, 0.506271, 0.828786, 0.300362, 1.651064246408177, 0.515992, 0.831158, 0.294279, 1.6587625199771945, 0.525776, 0.833491, 0.288127, 1.6664588307023491, 0.535621, 0.835785, 0.281908, 1.674157104271362, 0.545524, 0.838039, 0.275626, 1.6818553778403718, 0.555484, 0.840254, 0.269281, 1.6895516885655386, 0.565498, 0.84243, 0.262877, 1.6972499621345525, 0.575563, 0.844566, 0.256415, 1.704946272859715, 0.585678, 0.846661, 0.249897, 1.7126445464287323, 0.595839, 0.848717, 0.243329, 1.720340857153891, 0.606045, 0.850733, 0.236712, 1.7280391307229044, 0.616293, 0.852709, 0.230052, 1.7357374042919211, 0.626579, 0.854645, 0.223353, 1.7434337150170807, 0.636902, 0.856542, 0.21662, 1.7511319885860899, 0.647257, 0.8584, 0.209861, 1.7588282993112605, 0.657642, 0.860219, 0.203082, 1.766526572880269, 0.668054, 0.861999, 0.196293, 1.7742228836054363, 0.678489, 0.863742, 0.189503, 1.7819211571744422, 0.688944, 0.865448, 0.182725, 1.789619430743456, 0.699415, 0.867117, 0.175971, 1.7973157414686225, 0.709898, 0.868751, 0.169257, 1.805014015037631, 0.720391, 0.87035, 0.162603, 1.8127103257627972, 0.730889, 0.871916, 0.156029, 1.820408599331811, 0.741388, 0.873449, 0.149561, 1.8281049100569746, 0.751884, 0.874951, 0.143228, 1.8358031836259832, 0.762373, 0.876424, 0.137064, 1.84349949435115, 0.772852, 0.877868, 0.131109, 1.851197767920163, 0.783315, 0.879285, 0.125405, 1.8588960414891738, 0.79376, 0.880678, 0.120005, 1.8665923522143328, 0.804182, 0.882046, 0.114965, 1.874290625783349, 0.814576, 0.883393, 0.110347, 1.8819869365085125, 0.82494, 0.88472, 0.106217, 1.8896852100775288, 0.83527, 0.886029, 0.102646, 1.8973815208026878, 0.845561, 0.887322, 0.099702, 1.9050797943717017, 0.85581, 0.888601, 0.097452, 1.9127780679407147, 0.866013, 0.889868, 0.095953, 1.9204743786658782, 0.876168, 0.891125, 0.09525, 1.9281726522348908, 0.886271, 0.892374, 0.095374, 1.9358689629600574, 0.89632, 0.893616, 0.096335, 1.9435672365290633, 0.906311, 0.894855, 0.098125, 1.9512635472542288, 0.916242, 0.896091, 0.100717, 1.9589618208232429, 0.926106, 0.89733, 0.104071, 1.9666600943922514, 0.935904, 0.89857, 0.108131, 1.974356405117415, 0.945636, 0.899815, 0.112838, 1.9820546786864257, 0.9553, 0.901065, 0.118128, 1.9897509894115903, 0.964894, 0.902323, 0.123941, 1.9974492629806087, 0.974417, 0.90359, 0.130215, 2.005145573705771, 0.983868, 0.904867, 0.136897, 2.0128438472747803, 0.993248, 0.906157, 0.143936]
rhoLUT.NanColor = [1.0, 0.0, 0.0]
rhoLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'rho'
rhoPWF = GetOpacityTransferFunction('rho')
rhoPWF.Points = [0.05, 0.0, 0.5, 0.0, 2.0128438472747803, 1.0, 0.5, 0.0]
rhoPWF.ScalarRangeInitialized = 1

# change representation type
kh_mean_0hdf5Display.SetRepresentationType('Volume')

# Rescale transfer function
rhoLUT.RescaleTransferFunction(1.2, 2.1)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(1.2, 2.1)

# current camera placement for renderView1
renderView1.CameraPosition = [1089.2032867979851, 1400.3366614711433, 1213.538811793876]
renderView1.CameraFocalPoint = [255.5, 255.5, 255.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 442.53898133384814

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/kh/stats/p0_1/kh_mean_512_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
kh_mean_0hdf5_1 = NetCDFReader(FileName=['/scratch/snx3000/klye/3druns_new/kelvinhelmholtz_3d_tube/stats/p0_1/N256/kh_mean_0.hdf5'])
kh_mean_0hdf5_1.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(kh_mean_0hdf5, renderView1)

# show data in view
kh_mean_0hdf5_1Display = Show(kh_mean_0hdf5_1, renderView1)

# trace defaults for the display properties.
kh_mean_0hdf5_1Display.Representation = 'Outline'
kh_mean_0hdf5_1Display.ColorArrayName = [None, '']
kh_mean_0hdf5_1Display.OSPRayScaleArray = 'E'
kh_mean_0hdf5_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
kh_mean_0hdf5_1Display.SelectOrientationVectors = 'E'
kh_mean_0hdf5_1Display.ScaleFactor = 25.5
kh_mean_0hdf5_1Display.SelectScaleArray = 'E'
kh_mean_0hdf5_1Display.GlyphType = 'Arrow'
kh_mean_0hdf5_1Display.GlyphTableIndexArray = 'E'
kh_mean_0hdf5_1Display.GaussianRadius = 1.2750000000000001
kh_mean_0hdf5_1Display.SetScaleArray = ['POINTS', 'E']
kh_mean_0hdf5_1Display.ScaleTransferFunction = 'PiecewiseFunction'
kh_mean_0hdf5_1Display.OpacityArray = ['POINTS', 'E']
kh_mean_0hdf5_1Display.OpacityTransferFunction = 'PiecewiseFunction'
kh_mean_0hdf5_1Display.DataAxesGrid = 'GridAxesRepresentation'
kh_mean_0hdf5_1Display.SelectionCellLabelFontFile = ''
kh_mean_0hdf5_1Display.SelectionPointLabelFontFile = ''
kh_mean_0hdf5_1Display.PolarAxes = 'PolarAxesRepresentation'
kh_mean_0hdf5_1Display.ScalarOpacityUnitDistance = 1.7320508075688774
kh_mean_0hdf5_1Display.Slice = 127

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
kh_mean_0hdf5_1Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_1Display.DataAxesGrid.XTitleFontFile = ''
kh_mean_0hdf5_1Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_1Display.DataAxesGrid.YTitleFontFile = ''
kh_mean_0hdf5_1Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_1Display.DataAxesGrid.ZTitleFontFile = ''
kh_mean_0hdf5_1Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_1Display.DataAxesGrid.XLabelFontFile = ''
kh_mean_0hdf5_1Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_1Display.DataAxesGrid.YLabelFontFile = ''
kh_mean_0hdf5_1Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
kh_mean_0hdf5_1Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_1Display.PolarAxes.PolarAxisTitleFontFile = ''
kh_mean_0hdf5_1Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_1Display.PolarAxes.PolarAxisLabelFontFile = ''
kh_mean_0hdf5_1Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_1Display.PolarAxes.LastRadialAxisTextFontFile = ''
kh_mean_0hdf5_1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(kh_mean_0hdf5_1Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
kh_mean_0hdf5_1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
kh_mean_0hdf5_1Display.SetScalarBarVisibility(renderView1, True)

# change representation type
kh_mean_0hdf5_1Display.SetRepresentationType('Volume')

# Rescale transfer function
rhoLUT.RescaleTransferFunction(1.2, 2.1)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(1.2, 2.1)

# current camera placement for renderView1
renderView1.CameraPosition = [543.5358867582901, 698.7981383075178, 605.5819902298207]
renderView1.CameraFocalPoint = [127.5, 127.5, 127.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 220.83647796503186

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/kh/stats/p0_1/kh_mean_256_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
kh_mean_0hdf5_2 = NetCDFReader(FileName=['/scratch/snx3000/klye/3druns_new/kelvinhelmholtz_3d_tube/stats/p0_1/N128/kh_mean_0.hdf5'])
kh_mean_0hdf5_2.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(kh_mean_0hdf5_1, renderView1)

# show data in view
kh_mean_0hdf5_2Display = Show(kh_mean_0hdf5_2, renderView1)

# trace defaults for the display properties.
kh_mean_0hdf5_2Display.Representation = 'Outline'
kh_mean_0hdf5_2Display.ColorArrayName = [None, '']
kh_mean_0hdf5_2Display.OSPRayScaleArray = 'E'
kh_mean_0hdf5_2Display.OSPRayScaleFunction = 'PiecewiseFunction'
kh_mean_0hdf5_2Display.SelectOrientationVectors = 'E'
kh_mean_0hdf5_2Display.ScaleFactor = 12.700000000000001
kh_mean_0hdf5_2Display.SelectScaleArray = 'E'
kh_mean_0hdf5_2Display.GlyphType = 'Arrow'
kh_mean_0hdf5_2Display.GlyphTableIndexArray = 'E'
kh_mean_0hdf5_2Display.GaussianRadius = 0.635
kh_mean_0hdf5_2Display.SetScaleArray = ['POINTS', 'E']
kh_mean_0hdf5_2Display.ScaleTransferFunction = 'PiecewiseFunction'
kh_mean_0hdf5_2Display.OpacityArray = ['POINTS', 'E']
kh_mean_0hdf5_2Display.OpacityTransferFunction = 'PiecewiseFunction'
kh_mean_0hdf5_2Display.DataAxesGrid = 'GridAxesRepresentation'
kh_mean_0hdf5_2Display.SelectionCellLabelFontFile = ''
kh_mean_0hdf5_2Display.SelectionPointLabelFontFile = ''
kh_mean_0hdf5_2Display.PolarAxes = 'PolarAxesRepresentation'
kh_mean_0hdf5_2Display.ScalarOpacityUnitDistance = 1.732050807568877
kh_mean_0hdf5_2Display.Slice = 63

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
kh_mean_0hdf5_2Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_2Display.DataAxesGrid.XTitleFontFile = ''
kh_mean_0hdf5_2Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_2Display.DataAxesGrid.YTitleFontFile = ''
kh_mean_0hdf5_2Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_2Display.DataAxesGrid.ZTitleFontFile = ''
kh_mean_0hdf5_2Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_2Display.DataAxesGrid.XLabelFontFile = ''
kh_mean_0hdf5_2Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_2Display.DataAxesGrid.YLabelFontFile = ''
kh_mean_0hdf5_2Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_2Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
kh_mean_0hdf5_2Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_2Display.PolarAxes.PolarAxisTitleFontFile = ''
kh_mean_0hdf5_2Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_2Display.PolarAxes.PolarAxisLabelFontFile = ''
kh_mean_0hdf5_2Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_2Display.PolarAxes.LastRadialAxisTextFontFile = ''
kh_mean_0hdf5_2Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(kh_mean_0hdf5_2Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
kh_mean_0hdf5_2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
kh_mean_0hdf5_2Display.SetScalarBarVisibility(renderView1, True)

# change representation type
kh_mean_0hdf5_2Display.SetRepresentationType('Volume')

# Rescale transfer function
rhoLUT.RescaleTransferFunction(1.2, 2.1)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(1.2, 2.1)

# current camera placement for renderView1
renderView1.CameraPosition = [270.7021867384425, 348.0288767257049, 301.60357944779304]
renderView1.CameraFocalPoint = [63.5, 63.5, 63.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 109.9852262806237

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/kh/stats/p0_1/kh_mean_128_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
kh_mean_0hdf5_3 = NetCDFReader(FileName=['/scratch/snx3000/klye/3druns_new/kelvinhelmholtz_3d_tube/stats/p0_1/N64/kh_mean_0.hdf5'])
kh_mean_0hdf5_3.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(kh_mean_0hdf5_2, renderView1)

# show data in view
kh_mean_0hdf5_3Display = Show(kh_mean_0hdf5_3, renderView1)

# trace defaults for the display properties.
kh_mean_0hdf5_3Display.Representation = 'Outline'
kh_mean_0hdf5_3Display.ColorArrayName = [None, '']
kh_mean_0hdf5_3Display.OSPRayScaleArray = 'E'
kh_mean_0hdf5_3Display.OSPRayScaleFunction = 'PiecewiseFunction'
kh_mean_0hdf5_3Display.SelectOrientationVectors = 'E'
kh_mean_0hdf5_3Display.ScaleFactor = 6.300000000000001
kh_mean_0hdf5_3Display.SelectScaleArray = 'E'
kh_mean_0hdf5_3Display.GlyphType = 'Arrow'
kh_mean_0hdf5_3Display.GlyphTableIndexArray = 'E'
kh_mean_0hdf5_3Display.GaussianRadius = 0.315
kh_mean_0hdf5_3Display.SetScaleArray = ['POINTS', 'E']
kh_mean_0hdf5_3Display.ScaleTransferFunction = 'PiecewiseFunction'
kh_mean_0hdf5_3Display.OpacityArray = ['POINTS', 'E']
kh_mean_0hdf5_3Display.OpacityTransferFunction = 'PiecewiseFunction'
kh_mean_0hdf5_3Display.DataAxesGrid = 'GridAxesRepresentation'
kh_mean_0hdf5_3Display.SelectionCellLabelFontFile = ''
kh_mean_0hdf5_3Display.SelectionPointLabelFontFile = ''
kh_mean_0hdf5_3Display.PolarAxes = 'PolarAxesRepresentation'
kh_mean_0hdf5_3Display.ScalarOpacityUnitDistance = 1.7320508075688774
kh_mean_0hdf5_3Display.Slice = 31

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
kh_mean_0hdf5_3Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_3Display.DataAxesGrid.XTitleFontFile = ''
kh_mean_0hdf5_3Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_3Display.DataAxesGrid.YTitleFontFile = ''
kh_mean_0hdf5_3Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_3Display.DataAxesGrid.ZTitleFontFile = ''
kh_mean_0hdf5_3Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_3Display.DataAxesGrid.XLabelFontFile = ''
kh_mean_0hdf5_3Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_3Display.DataAxesGrid.YLabelFontFile = ''
kh_mean_0hdf5_3Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_3Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
kh_mean_0hdf5_3Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_3Display.PolarAxes.PolarAxisTitleFontFile = ''
kh_mean_0hdf5_3Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_3Display.PolarAxes.PolarAxisLabelFontFile = ''
kh_mean_0hdf5_3Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_3Display.PolarAxes.LastRadialAxisTextFontFile = ''
kh_mean_0hdf5_3Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_3Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(kh_mean_0hdf5_3Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
kh_mean_0hdf5_3Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
kh_mean_0hdf5_3Display.SetScalarBarVisibility(renderView1, True)

# change representation type
kh_mean_0hdf5_3Display.SetRepresentationType('Volume')

# Rescale transfer function
rhoLUT.RescaleTransferFunction(1.2, 2.1)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(1.2, 2.1)

# current camera placement for renderView1
renderView1.CameraPosition = [134.28533672851873, 172.6442459347985, 149.61437405677924]
renderView1.CameraFocalPoint = [31.5, 31.5, 31.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 54.559600438419636

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/kh/stats/p0_1/kh_mean_64_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# hide data in view
Hide(kh_mean_0hdf5_3, renderView1)

# create a new 'NetCDF Reader'
kh_mean_0hdf5_4 = NetCDFReader(FileName=['/scratch/snx3000/klye/3druns_new/kelvinhelmholtz_3d_tube/stats/p0_01/N512/kh_mean_0.hdf5'])
kh_mean_0hdf5_4.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# show data in view
kh_mean_0hdf5_4Display = Show(kh_mean_0hdf5_4, renderView1)

# trace defaults for the display properties.
kh_mean_0hdf5_4Display.Representation = 'Outline'
kh_mean_0hdf5_4Display.ColorArrayName = [None, '']
kh_mean_0hdf5_4Display.OSPRayScaleArray = 'E'
kh_mean_0hdf5_4Display.OSPRayScaleFunction = 'PiecewiseFunction'
kh_mean_0hdf5_4Display.SelectOrientationVectors = 'E'
kh_mean_0hdf5_4Display.ScaleFactor = 51.1
kh_mean_0hdf5_4Display.SelectScaleArray = 'E'
kh_mean_0hdf5_4Display.GlyphType = 'Arrow'
kh_mean_0hdf5_4Display.GlyphTableIndexArray = 'E'
kh_mean_0hdf5_4Display.GaussianRadius = 2.555
kh_mean_0hdf5_4Display.SetScaleArray = ['POINTS', 'E']
kh_mean_0hdf5_4Display.ScaleTransferFunction = 'PiecewiseFunction'
kh_mean_0hdf5_4Display.OpacityArray = ['POINTS', 'E']
kh_mean_0hdf5_4Display.OpacityTransferFunction = 'PiecewiseFunction'
kh_mean_0hdf5_4Display.DataAxesGrid = 'GridAxesRepresentation'
kh_mean_0hdf5_4Display.SelectionCellLabelFontFile = ''
kh_mean_0hdf5_4Display.SelectionPointLabelFontFile = ''
kh_mean_0hdf5_4Display.PolarAxes = 'PolarAxesRepresentation'
kh_mean_0hdf5_4Display.ScalarOpacityUnitDistance = 1.732050807568877
kh_mean_0hdf5_4Display.Slice = 255

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
kh_mean_0hdf5_4Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_4Display.DataAxesGrid.XTitleFontFile = ''
kh_mean_0hdf5_4Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_4Display.DataAxesGrid.YTitleFontFile = ''
kh_mean_0hdf5_4Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_4Display.DataAxesGrid.ZTitleFontFile = ''
kh_mean_0hdf5_4Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_4Display.DataAxesGrid.XLabelFontFile = ''
kh_mean_0hdf5_4Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_4Display.DataAxesGrid.YLabelFontFile = ''
kh_mean_0hdf5_4Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_4Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
kh_mean_0hdf5_4Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_4Display.PolarAxes.PolarAxisTitleFontFile = ''
kh_mean_0hdf5_4Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_4Display.PolarAxes.PolarAxisLabelFontFile = ''
kh_mean_0hdf5_4Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_4Display.PolarAxes.LastRadialAxisTextFontFile = ''
kh_mean_0hdf5_4Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_4Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(kh_mean_0hdf5_4Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
kh_mean_0hdf5_4Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
kh_mean_0hdf5_4Display.SetScalarBarVisibility(renderView1, True)

# change representation type
kh_mean_0hdf5_4Display.SetRepresentationType('Volume')

# Rescale transfer function
rhoLUT.RescaleTransferFunction(1.2, 2.1)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(1.2, 2.1)

# current camera placement for renderView1
renderView1.CameraPosition = [1089.2032867979851, 1400.3366614711433, 1213.538811793876]
renderView1.CameraFocalPoint = [255.5, 255.5, 255.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 442.53898133384814

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/kh/stats/p0_01/kh_mean_512_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
kh_mean_0hdf5_5 = NetCDFReader(FileName=['/scratch/snx3000/klye/3druns_new/kelvinhelmholtz_3d_tube/stats/p0_01/N256/kh_mean_0.hdf5'])
kh_mean_0hdf5_5.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(kh_mean_0hdf5_4, renderView1)

# show data in view
kh_mean_0hdf5_5Display = Show(kh_mean_0hdf5_5, renderView1)

# trace defaults for the display properties.
kh_mean_0hdf5_5Display.Representation = 'Outline'
kh_mean_0hdf5_5Display.ColorArrayName = [None, '']
kh_mean_0hdf5_5Display.OSPRayScaleArray = 'E'
kh_mean_0hdf5_5Display.OSPRayScaleFunction = 'PiecewiseFunction'
kh_mean_0hdf5_5Display.SelectOrientationVectors = 'E'
kh_mean_0hdf5_5Display.ScaleFactor = 25.5
kh_mean_0hdf5_5Display.SelectScaleArray = 'E'
kh_mean_0hdf5_5Display.GlyphType = 'Arrow'
kh_mean_0hdf5_5Display.GlyphTableIndexArray = 'E'
kh_mean_0hdf5_5Display.GaussianRadius = 1.2750000000000001
kh_mean_0hdf5_5Display.SetScaleArray = ['POINTS', 'E']
kh_mean_0hdf5_5Display.ScaleTransferFunction = 'PiecewiseFunction'
kh_mean_0hdf5_5Display.OpacityArray = ['POINTS', 'E']
kh_mean_0hdf5_5Display.OpacityTransferFunction = 'PiecewiseFunction'
kh_mean_0hdf5_5Display.DataAxesGrid = 'GridAxesRepresentation'
kh_mean_0hdf5_5Display.SelectionCellLabelFontFile = ''
kh_mean_0hdf5_5Display.SelectionPointLabelFontFile = ''
kh_mean_0hdf5_5Display.PolarAxes = 'PolarAxesRepresentation'
kh_mean_0hdf5_5Display.ScalarOpacityUnitDistance = 1.7320508075688774
kh_mean_0hdf5_5Display.Slice = 127

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
kh_mean_0hdf5_5Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_5Display.DataAxesGrid.XTitleFontFile = ''
kh_mean_0hdf5_5Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_5Display.DataAxesGrid.YTitleFontFile = ''
kh_mean_0hdf5_5Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_5Display.DataAxesGrid.ZTitleFontFile = ''
kh_mean_0hdf5_5Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_5Display.DataAxesGrid.XLabelFontFile = ''
kh_mean_0hdf5_5Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_5Display.DataAxesGrid.YLabelFontFile = ''
kh_mean_0hdf5_5Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_5Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
kh_mean_0hdf5_5Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_5Display.PolarAxes.PolarAxisTitleFontFile = ''
kh_mean_0hdf5_5Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_5Display.PolarAxes.PolarAxisLabelFontFile = ''
kh_mean_0hdf5_5Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_5Display.PolarAxes.LastRadialAxisTextFontFile = ''
kh_mean_0hdf5_5Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_5Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(kh_mean_0hdf5_5Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
kh_mean_0hdf5_5Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
kh_mean_0hdf5_5Display.SetScalarBarVisibility(renderView1, True)

# change representation type
kh_mean_0hdf5_5Display.SetRepresentationType('Volume')

# Rescale transfer function
rhoLUT.RescaleTransferFunction(1.2, 2.1)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(1.2, 2.1)

# current camera placement for renderView1
renderView1.CameraPosition = [543.5358867582901, 698.7981383075178, 605.5819902298207]
renderView1.CameraFocalPoint = [127.5, 127.5, 127.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 220.83647796503186

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/kh/stats/p0_01/kh_mean_256_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
kh_mean_0hdf5_6 = NetCDFReader(FileName=['/scratch/snx3000/klye/3druns_new/kelvinhelmholtz_3d_tube/stats/p0_01/N128/kh_mean_0.hdf5'])
kh_mean_0hdf5_6.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(kh_mean_0hdf5_5, renderView1)

# show data in view
kh_mean_0hdf5_6Display = Show(kh_mean_0hdf5_6, renderView1)

# trace defaults for the display properties.
kh_mean_0hdf5_6Display.Representation = 'Outline'
kh_mean_0hdf5_6Display.ColorArrayName = [None, '']
kh_mean_0hdf5_6Display.OSPRayScaleArray = 'E'
kh_mean_0hdf5_6Display.OSPRayScaleFunction = 'PiecewiseFunction'
kh_mean_0hdf5_6Display.SelectOrientationVectors = 'E'
kh_mean_0hdf5_6Display.ScaleFactor = 12.700000000000001
kh_mean_0hdf5_6Display.SelectScaleArray = 'E'
kh_mean_0hdf5_6Display.GlyphType = 'Arrow'
kh_mean_0hdf5_6Display.GlyphTableIndexArray = 'E'
kh_mean_0hdf5_6Display.GaussianRadius = 0.635
kh_mean_0hdf5_6Display.SetScaleArray = ['POINTS', 'E']
kh_mean_0hdf5_6Display.ScaleTransferFunction = 'PiecewiseFunction'
kh_mean_0hdf5_6Display.OpacityArray = ['POINTS', 'E']
kh_mean_0hdf5_6Display.OpacityTransferFunction = 'PiecewiseFunction'
kh_mean_0hdf5_6Display.DataAxesGrid = 'GridAxesRepresentation'
kh_mean_0hdf5_6Display.SelectionCellLabelFontFile = ''
kh_mean_0hdf5_6Display.SelectionPointLabelFontFile = ''
kh_mean_0hdf5_6Display.PolarAxes = 'PolarAxesRepresentation'
kh_mean_0hdf5_6Display.ScalarOpacityUnitDistance = 1.732050807568877
kh_mean_0hdf5_6Display.Slice = 63

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
kh_mean_0hdf5_6Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_6Display.DataAxesGrid.XTitleFontFile = ''
kh_mean_0hdf5_6Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_6Display.DataAxesGrid.YTitleFontFile = ''
kh_mean_0hdf5_6Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_6Display.DataAxesGrid.ZTitleFontFile = ''
kh_mean_0hdf5_6Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_6Display.DataAxesGrid.XLabelFontFile = ''
kh_mean_0hdf5_6Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_6Display.DataAxesGrid.YLabelFontFile = ''
kh_mean_0hdf5_6Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_6Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
kh_mean_0hdf5_6Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_6Display.PolarAxes.PolarAxisTitleFontFile = ''
kh_mean_0hdf5_6Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_6Display.PolarAxes.PolarAxisLabelFontFile = ''
kh_mean_0hdf5_6Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_6Display.PolarAxes.LastRadialAxisTextFontFile = ''
kh_mean_0hdf5_6Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_6Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(kh_mean_0hdf5_6Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
kh_mean_0hdf5_6Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
kh_mean_0hdf5_6Display.SetScalarBarVisibility(renderView1, True)

# change representation type
kh_mean_0hdf5_6Display.SetRepresentationType('Volume')

# Rescale transfer function
rhoLUT.RescaleTransferFunction(1.2, 2.1)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(1.2, 2.1)

# current camera placement for renderView1
renderView1.CameraPosition = [270.7021867384425, 348.0288767257049, 301.60357944779304]
renderView1.CameraFocalPoint = [63.5, 63.5, 63.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 109.9852262806237

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/kh/stats/p0_01/kh_mean_128_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
kh_mean_0hdf5_7 = NetCDFReader(FileName=['/scratch/snx3000/klye/3druns_new/kelvinhelmholtz_3d_tube/stats/p0_01/N64/kh_mean_0.hdf5'])
kh_mean_0hdf5_7.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(kh_mean_0hdf5_6, renderView1)

# show data in view
kh_mean_0hdf5_7Display = Show(kh_mean_0hdf5_7, renderView1)

# trace defaults for the display properties.
kh_mean_0hdf5_7Display.Representation = 'Outline'
kh_mean_0hdf5_7Display.ColorArrayName = [None, '']
kh_mean_0hdf5_7Display.OSPRayScaleArray = 'E'
kh_mean_0hdf5_7Display.OSPRayScaleFunction = 'PiecewiseFunction'
kh_mean_0hdf5_7Display.SelectOrientationVectors = 'E'
kh_mean_0hdf5_7Display.ScaleFactor = 6.300000000000001
kh_mean_0hdf5_7Display.SelectScaleArray = 'E'
kh_mean_0hdf5_7Display.GlyphType = 'Arrow'
kh_mean_0hdf5_7Display.GlyphTableIndexArray = 'E'
kh_mean_0hdf5_7Display.GaussianRadius = 0.315
kh_mean_0hdf5_7Display.SetScaleArray = ['POINTS', 'E']
kh_mean_0hdf5_7Display.ScaleTransferFunction = 'PiecewiseFunction'
kh_mean_0hdf5_7Display.OpacityArray = ['POINTS', 'E']
kh_mean_0hdf5_7Display.OpacityTransferFunction = 'PiecewiseFunction'
kh_mean_0hdf5_7Display.DataAxesGrid = 'GridAxesRepresentation'
kh_mean_0hdf5_7Display.SelectionCellLabelFontFile = ''
kh_mean_0hdf5_7Display.SelectionPointLabelFontFile = ''
kh_mean_0hdf5_7Display.PolarAxes = 'PolarAxesRepresentation'
kh_mean_0hdf5_7Display.ScalarOpacityUnitDistance = 1.7320508075688774
kh_mean_0hdf5_7Display.Slice = 31

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
kh_mean_0hdf5_7Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_7Display.DataAxesGrid.XTitleFontFile = ''
kh_mean_0hdf5_7Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_7Display.DataAxesGrid.YTitleFontFile = ''
kh_mean_0hdf5_7Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_7Display.DataAxesGrid.ZTitleFontFile = ''
kh_mean_0hdf5_7Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_7Display.DataAxesGrid.XLabelFontFile = ''
kh_mean_0hdf5_7Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_7Display.DataAxesGrid.YLabelFontFile = ''
kh_mean_0hdf5_7Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_7Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
kh_mean_0hdf5_7Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_7Display.PolarAxes.PolarAxisTitleFontFile = ''
kh_mean_0hdf5_7Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_7Display.PolarAxes.PolarAxisLabelFontFile = ''
kh_mean_0hdf5_7Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_7Display.PolarAxes.LastRadialAxisTextFontFile = ''
kh_mean_0hdf5_7Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_mean_0hdf5_7Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(kh_mean_0hdf5_7Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
kh_mean_0hdf5_7Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
kh_mean_0hdf5_7Display.SetScalarBarVisibility(renderView1, True)

# change representation type
kh_mean_0hdf5_7Display.SetRepresentationType('Volume')

# Rescale transfer function
rhoLUT.RescaleTransferFunction(1.2, 2.1)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(1.2, 2.1)

# current camera placement for renderView1
renderView1.CameraPosition = [134.28533672851873, 172.6442459347985, 149.61437405677924]
renderView1.CameraFocalPoint = [31.5, 31.5, 31.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 54.559600438419636

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/kh/stats/p0_01/kh_mean_64_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# hide data in view
Hide(kh_mean_0hdf5_7, renderView1)

# create a new 'NetCDF Reader'
kh_variance_0hdf5 = NetCDFReader(FileName=['/scratch/snx3000/klye/3druns_new/kelvinhelmholtz_3d_tube/stats/p0_01/N512/kh_variance_0.hdf5'])
kh_variance_0hdf5.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# show data in view
kh_variance_0hdf5Display = Show(kh_variance_0hdf5, renderView1)

# trace defaults for the display properties.
kh_variance_0hdf5Display.Representation = 'Outline'
kh_variance_0hdf5Display.ColorArrayName = [None, '']
kh_variance_0hdf5Display.OSPRayScaleArray = 'E'
kh_variance_0hdf5Display.OSPRayScaleFunction = 'PiecewiseFunction'
kh_variance_0hdf5Display.SelectOrientationVectors = 'E'
kh_variance_0hdf5Display.ScaleFactor = 51.1
kh_variance_0hdf5Display.SelectScaleArray = 'E'
kh_variance_0hdf5Display.GlyphType = 'Arrow'
kh_variance_0hdf5Display.GlyphTableIndexArray = 'E'
kh_variance_0hdf5Display.GaussianRadius = 2.555
kh_variance_0hdf5Display.SetScaleArray = ['POINTS', 'E']
kh_variance_0hdf5Display.ScaleTransferFunction = 'PiecewiseFunction'
kh_variance_0hdf5Display.OpacityArray = ['POINTS', 'E']
kh_variance_0hdf5Display.OpacityTransferFunction = 'PiecewiseFunction'
kh_variance_0hdf5Display.DataAxesGrid = 'GridAxesRepresentation'
kh_variance_0hdf5Display.SelectionCellLabelFontFile = ''
kh_variance_0hdf5Display.SelectionPointLabelFontFile = ''
kh_variance_0hdf5Display.PolarAxes = 'PolarAxesRepresentation'
kh_variance_0hdf5Display.ScalarOpacityUnitDistance = 1.732050807568877
kh_variance_0hdf5Display.Slice = 255

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
kh_variance_0hdf5Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5Display.DataAxesGrid.XTitleFontFile = ''
kh_variance_0hdf5Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5Display.DataAxesGrid.YTitleFontFile = ''
kh_variance_0hdf5Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5Display.DataAxesGrid.ZTitleFontFile = ''
kh_variance_0hdf5Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5Display.DataAxesGrid.XLabelFontFile = ''
kh_variance_0hdf5Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5Display.DataAxesGrid.YLabelFontFile = ''
kh_variance_0hdf5Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
kh_variance_0hdf5Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5Display.PolarAxes.PolarAxisTitleFontFile = ''
kh_variance_0hdf5Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5Display.PolarAxes.PolarAxisLabelFontFile = ''
kh_variance_0hdf5Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5Display.PolarAxes.LastRadialAxisTextFontFile = ''
kh_variance_0hdf5Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(kh_mean_0hdf5)

# destroy kh_mean_0hdf5
Delete(kh_mean_0hdf5)
del kh_mean_0hdf5

# set active source
SetActiveSource(kh_mean_0hdf5_1)

# destroy kh_mean_0hdf5_1
Delete(kh_mean_0hdf5_1)
del kh_mean_0hdf5_1

# set active source
SetActiveSource(kh_mean_0hdf5_2)

# destroy kh_mean_0hdf5_2
Delete(kh_mean_0hdf5_2)
del kh_mean_0hdf5_2

# set active source
SetActiveSource(kh_mean_0hdf5_3)

# destroy kh_mean_0hdf5_3
Delete(kh_mean_0hdf5_3)
del kh_mean_0hdf5_3

# set active source
SetActiveSource(kh_mean_0hdf5_4)

# destroy kh_mean_0hdf5_4
Delete(kh_mean_0hdf5_4)
del kh_mean_0hdf5_4

# set active source
SetActiveSource(kh_mean_0hdf5_5)

# destroy kh_mean_0hdf5_5
Delete(kh_mean_0hdf5_5)
del kh_mean_0hdf5_5

# set active source
SetActiveSource(kh_variance_0hdf5)

# set scalar coloring
ColorBy(kh_variance_0hdf5Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
kh_variance_0hdf5Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
kh_variance_0hdf5Display.SetScalarBarVisibility(renderView1, True)

# change representation type
kh_variance_0hdf5Display.SetRepresentationType('Volume')

# rescale color and/or opacity maps used to exactly fit the current data range
kh_variance_0hdf5Display.RescaleTransferFunctionToDataRange(False, True)

# Rescale transfer function
rhoLUT.RescaleTransferFunction(0.0, 0.08)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(0.0, 0.08)

# current camera placement for renderView1
renderView1.CameraPosition = [1089.2032867979851, 1400.3366614711433, 1213.538811793876]
renderView1.CameraFocalPoint = [255.5, 255.5, 255.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 442.53898133384814

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/kh/stats/p0_01/kh_variance_512_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
kh_variance_0hdf5_1 = NetCDFReader(FileName=['/scratch/snx3000/klye/3druns_new/kelvinhelmholtz_3d_tube/stats/p0_01/N256/kh_variance_0.hdf5'])
kh_variance_0hdf5_1.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(kh_variance_0hdf5, renderView1)

# show data in view
kh_variance_0hdf5_1Display = Show(kh_variance_0hdf5_1, renderView1)

# trace defaults for the display properties.
kh_variance_0hdf5_1Display.Representation = 'Outline'
kh_variance_0hdf5_1Display.ColorArrayName = [None, '']
kh_variance_0hdf5_1Display.OSPRayScaleArray = 'E'
kh_variance_0hdf5_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
kh_variance_0hdf5_1Display.SelectOrientationVectors = 'E'
kh_variance_0hdf5_1Display.ScaleFactor = 25.5
kh_variance_0hdf5_1Display.SelectScaleArray = 'E'
kh_variance_0hdf5_1Display.GlyphType = 'Arrow'
kh_variance_0hdf5_1Display.GlyphTableIndexArray = 'E'
kh_variance_0hdf5_1Display.GaussianRadius = 1.2750000000000001
kh_variance_0hdf5_1Display.SetScaleArray = ['POINTS', 'E']
kh_variance_0hdf5_1Display.ScaleTransferFunction = 'PiecewiseFunction'
kh_variance_0hdf5_1Display.OpacityArray = ['POINTS', 'E']
kh_variance_0hdf5_1Display.OpacityTransferFunction = 'PiecewiseFunction'
kh_variance_0hdf5_1Display.DataAxesGrid = 'GridAxesRepresentation'
kh_variance_0hdf5_1Display.SelectionCellLabelFontFile = ''
kh_variance_0hdf5_1Display.SelectionPointLabelFontFile = ''
kh_variance_0hdf5_1Display.PolarAxes = 'PolarAxesRepresentation'
kh_variance_0hdf5_1Display.ScalarOpacityUnitDistance = 1.7320508075688774
kh_variance_0hdf5_1Display.Slice = 127

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
kh_variance_0hdf5_1Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_1Display.DataAxesGrid.XTitleFontFile = ''
kh_variance_0hdf5_1Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_1Display.DataAxesGrid.YTitleFontFile = ''
kh_variance_0hdf5_1Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_1Display.DataAxesGrid.ZTitleFontFile = ''
kh_variance_0hdf5_1Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_1Display.DataAxesGrid.XLabelFontFile = ''
kh_variance_0hdf5_1Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_1Display.DataAxesGrid.YLabelFontFile = ''
kh_variance_0hdf5_1Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
kh_variance_0hdf5_1Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_1Display.PolarAxes.PolarAxisTitleFontFile = ''
kh_variance_0hdf5_1Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_1Display.PolarAxes.PolarAxisLabelFontFile = ''
kh_variance_0hdf5_1Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_1Display.PolarAxes.LastRadialAxisTextFontFile = ''
kh_variance_0hdf5_1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(kh_variance_0hdf5_1Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
kh_variance_0hdf5_1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
kh_variance_0hdf5_1Display.SetScalarBarVisibility(renderView1, True)

# change representation type
kh_variance_0hdf5_1Display.SetRepresentationType('Volume')

# Rescale transfer function
rhoLUT.RescaleTransferFunction(0.0, 0.08)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(0.0, 0.08)

# current camera placement for renderView1
renderView1.CameraPosition = [543.5358867582901, 698.7981383075178, 605.5819902298207]
renderView1.CameraFocalPoint = [127.5, 127.5, 127.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 220.83647796503186

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/kh/stats/p0_01/kh_variance_256_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
kh_variance_0hdf5_2 = NetCDFReader(FileName=['/scratch/snx3000/klye/3druns_new/kelvinhelmholtz_3d_tube/stats/p0_01/N128/kh_variance_0.hdf5'])
kh_variance_0hdf5_2.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(kh_variance_0hdf5_1, renderView1)

# show data in view
kh_variance_0hdf5_2Display = Show(kh_variance_0hdf5_2, renderView1)

# trace defaults for the display properties.
kh_variance_0hdf5_2Display.Representation = 'Outline'
kh_variance_0hdf5_2Display.ColorArrayName = [None, '']
kh_variance_0hdf5_2Display.OSPRayScaleArray = 'E'
kh_variance_0hdf5_2Display.OSPRayScaleFunction = 'PiecewiseFunction'
kh_variance_0hdf5_2Display.SelectOrientationVectors = 'E'
kh_variance_0hdf5_2Display.ScaleFactor = 12.700000000000001
kh_variance_0hdf5_2Display.SelectScaleArray = 'E'
kh_variance_0hdf5_2Display.GlyphType = 'Arrow'
kh_variance_0hdf5_2Display.GlyphTableIndexArray = 'E'
kh_variance_0hdf5_2Display.GaussianRadius = 0.635
kh_variance_0hdf5_2Display.SetScaleArray = ['POINTS', 'E']
kh_variance_0hdf5_2Display.ScaleTransferFunction = 'PiecewiseFunction'
kh_variance_0hdf5_2Display.OpacityArray = ['POINTS', 'E']
kh_variance_0hdf5_2Display.OpacityTransferFunction = 'PiecewiseFunction'
kh_variance_0hdf5_2Display.DataAxesGrid = 'GridAxesRepresentation'
kh_variance_0hdf5_2Display.SelectionCellLabelFontFile = ''
kh_variance_0hdf5_2Display.SelectionPointLabelFontFile = ''
kh_variance_0hdf5_2Display.PolarAxes = 'PolarAxesRepresentation'
kh_variance_0hdf5_2Display.ScalarOpacityUnitDistance = 1.732050807568877
kh_variance_0hdf5_2Display.Slice = 63

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
kh_variance_0hdf5_2Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_2Display.DataAxesGrid.XTitleFontFile = ''
kh_variance_0hdf5_2Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_2Display.DataAxesGrid.YTitleFontFile = ''
kh_variance_0hdf5_2Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_2Display.DataAxesGrid.ZTitleFontFile = ''
kh_variance_0hdf5_2Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_2Display.DataAxesGrid.XLabelFontFile = ''
kh_variance_0hdf5_2Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_2Display.DataAxesGrid.YLabelFontFile = ''
kh_variance_0hdf5_2Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_2Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
kh_variance_0hdf5_2Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_2Display.PolarAxes.PolarAxisTitleFontFile = ''
kh_variance_0hdf5_2Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_2Display.PolarAxes.PolarAxisLabelFontFile = ''
kh_variance_0hdf5_2Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_2Display.PolarAxes.LastRadialAxisTextFontFile = ''
kh_variance_0hdf5_2Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(kh_variance_0hdf5_2Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
kh_variance_0hdf5_2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
kh_variance_0hdf5_2Display.SetScalarBarVisibility(renderView1, True)

# change representation type
kh_variance_0hdf5_2Display.SetRepresentationType('Volume')

# Rescale transfer function
rhoLUT.RescaleTransferFunction(0.0, 0.08)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(0.0, 0.08)

# current camera placement for renderView1
renderView1.CameraPosition = [270.7021867384425, 348.0288767257049, 301.60357944779304]
renderView1.CameraFocalPoint = [63.5, 63.5, 63.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 109.9852262806237

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/kh/stats/p0_01/kh_variance_128_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
kh_variance_0hdf5_3 = NetCDFReader(FileName=['/scratch/snx3000/klye/3druns_new/kelvinhelmholtz_3d_tube/stats/p0_01/N64/kh_variance_0.hdf5'])
kh_variance_0hdf5_3.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(kh_variance_0hdf5_2, renderView1)

# show data in view
kh_variance_0hdf5_3Display = Show(kh_variance_0hdf5_3, renderView1)

# trace defaults for the display properties.
kh_variance_0hdf5_3Display.Representation = 'Outline'
kh_variance_0hdf5_3Display.ColorArrayName = [None, '']
kh_variance_0hdf5_3Display.OSPRayScaleArray = 'E'
kh_variance_0hdf5_3Display.OSPRayScaleFunction = 'PiecewiseFunction'
kh_variance_0hdf5_3Display.SelectOrientationVectors = 'E'
kh_variance_0hdf5_3Display.ScaleFactor = 6.300000000000001
kh_variance_0hdf5_3Display.SelectScaleArray = 'E'
kh_variance_0hdf5_3Display.GlyphType = 'Arrow'
kh_variance_0hdf5_3Display.GlyphTableIndexArray = 'E'
kh_variance_0hdf5_3Display.GaussianRadius = 0.315
kh_variance_0hdf5_3Display.SetScaleArray = ['POINTS', 'E']
kh_variance_0hdf5_3Display.ScaleTransferFunction = 'PiecewiseFunction'
kh_variance_0hdf5_3Display.OpacityArray = ['POINTS', 'E']
kh_variance_0hdf5_3Display.OpacityTransferFunction = 'PiecewiseFunction'
kh_variance_0hdf5_3Display.DataAxesGrid = 'GridAxesRepresentation'
kh_variance_0hdf5_3Display.SelectionCellLabelFontFile = ''
kh_variance_0hdf5_3Display.SelectionPointLabelFontFile = ''
kh_variance_0hdf5_3Display.PolarAxes = 'PolarAxesRepresentation'
kh_variance_0hdf5_3Display.ScalarOpacityUnitDistance = 1.7320508075688774
kh_variance_0hdf5_3Display.Slice = 31

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
kh_variance_0hdf5_3Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_3Display.DataAxesGrid.XTitleFontFile = ''
kh_variance_0hdf5_3Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_3Display.DataAxesGrid.YTitleFontFile = ''
kh_variance_0hdf5_3Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_3Display.DataAxesGrid.ZTitleFontFile = ''
kh_variance_0hdf5_3Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_3Display.DataAxesGrid.XLabelFontFile = ''
kh_variance_0hdf5_3Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_3Display.DataAxesGrid.YLabelFontFile = ''
kh_variance_0hdf5_3Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_3Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
kh_variance_0hdf5_3Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_3Display.PolarAxes.PolarAxisTitleFontFile = ''
kh_variance_0hdf5_3Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_3Display.PolarAxes.PolarAxisLabelFontFile = ''
kh_variance_0hdf5_3Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_3Display.PolarAxes.LastRadialAxisTextFontFile = ''
kh_variance_0hdf5_3Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_3Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(kh_variance_0hdf5_3Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
kh_variance_0hdf5_3Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
kh_variance_0hdf5_3Display.SetScalarBarVisibility(renderView1, True)

# change representation type
kh_variance_0hdf5_3Display.SetRepresentationType('Volume')

# current camera placement for renderView1
renderView1.CameraPosition = [134.28533672851873, 172.6442459347985, 149.61437405677924]
renderView1.CameraFocalPoint = [31.5, 31.5, 31.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 54.559600438419636

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/kh/stats/p0_01/kh_variance_64_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
kh_variance_0hdf5_4 = NetCDFReader(FileName=['/scratch/snx3000/klye/3druns_new/kelvinhelmholtz_3d_tube/stats/p0_1/N512/kh_variance_0.hdf5'])
kh_variance_0hdf5_4.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(kh_variance_0hdf5_3, renderView1)

# show data in view
kh_variance_0hdf5_4Display = Show(kh_variance_0hdf5_4, renderView1)

# trace defaults for the display properties.
kh_variance_0hdf5_4Display.Representation = 'Outline'
kh_variance_0hdf5_4Display.ColorArrayName = [None, '']
kh_variance_0hdf5_4Display.OSPRayScaleArray = 'E'
kh_variance_0hdf5_4Display.OSPRayScaleFunction = 'PiecewiseFunction'
kh_variance_0hdf5_4Display.SelectOrientationVectors = 'E'
kh_variance_0hdf5_4Display.ScaleFactor = 51.1
kh_variance_0hdf5_4Display.SelectScaleArray = 'E'
kh_variance_0hdf5_4Display.GlyphType = 'Arrow'
kh_variance_0hdf5_4Display.GlyphTableIndexArray = 'E'
kh_variance_0hdf5_4Display.GaussianRadius = 2.555
kh_variance_0hdf5_4Display.SetScaleArray = ['POINTS', 'E']
kh_variance_0hdf5_4Display.ScaleTransferFunction = 'PiecewiseFunction'
kh_variance_0hdf5_4Display.OpacityArray = ['POINTS', 'E']
kh_variance_0hdf5_4Display.OpacityTransferFunction = 'PiecewiseFunction'
kh_variance_0hdf5_4Display.DataAxesGrid = 'GridAxesRepresentation'
kh_variance_0hdf5_4Display.SelectionCellLabelFontFile = ''
kh_variance_0hdf5_4Display.SelectionPointLabelFontFile = ''
kh_variance_0hdf5_4Display.PolarAxes = 'PolarAxesRepresentation'
kh_variance_0hdf5_4Display.ScalarOpacityUnitDistance = 1.732050807568877
kh_variance_0hdf5_4Display.Slice = 255

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
kh_variance_0hdf5_4Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_4Display.DataAxesGrid.XTitleFontFile = ''
kh_variance_0hdf5_4Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_4Display.DataAxesGrid.YTitleFontFile = ''
kh_variance_0hdf5_4Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_4Display.DataAxesGrid.ZTitleFontFile = ''
kh_variance_0hdf5_4Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_4Display.DataAxesGrid.XLabelFontFile = ''
kh_variance_0hdf5_4Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_4Display.DataAxesGrid.YLabelFontFile = ''
kh_variance_0hdf5_4Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_4Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
kh_variance_0hdf5_4Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_4Display.PolarAxes.PolarAxisTitleFontFile = ''
kh_variance_0hdf5_4Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_4Display.PolarAxes.PolarAxisLabelFontFile = ''
kh_variance_0hdf5_4Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_4Display.PolarAxes.LastRadialAxisTextFontFile = ''
kh_variance_0hdf5_4Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_4Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(kh_variance_0hdf5_4Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
kh_variance_0hdf5_4Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
kh_variance_0hdf5_4Display.SetScalarBarVisibility(renderView1, True)

# change representation type
kh_variance_0hdf5_4Display.SetRepresentationType('Volume')

# current camera placement for renderView1
renderView1.CameraPosition = [1089.2032867979851, 1400.3366614711433, 1213.538811793876]
renderView1.CameraFocalPoint = [255.5, 255.5, 255.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 442.53898133384814

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/kh/stats/p0_1/kh_variance_512_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
kh_variance_0hdf5_5 = NetCDFReader(FileName=['/scratch/snx3000/klye/3druns_new/kelvinhelmholtz_3d_tube/stats/p0_1/N256/kh_variance_0.hdf5'])
kh_variance_0hdf5_5.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(kh_variance_0hdf5_4, renderView1)

# show data in view
kh_variance_0hdf5_5Display = Show(kh_variance_0hdf5_5, renderView1)

# trace defaults for the display properties.
kh_variance_0hdf5_5Display.Representation = 'Outline'
kh_variance_0hdf5_5Display.ColorArrayName = [None, '']
kh_variance_0hdf5_5Display.OSPRayScaleArray = 'E'
kh_variance_0hdf5_5Display.OSPRayScaleFunction = 'PiecewiseFunction'
kh_variance_0hdf5_5Display.SelectOrientationVectors = 'E'
kh_variance_0hdf5_5Display.ScaleFactor = 25.5
kh_variance_0hdf5_5Display.SelectScaleArray = 'E'
kh_variance_0hdf5_5Display.GlyphType = 'Arrow'
kh_variance_0hdf5_5Display.GlyphTableIndexArray = 'E'
kh_variance_0hdf5_5Display.GaussianRadius = 1.2750000000000001
kh_variance_0hdf5_5Display.SetScaleArray = ['POINTS', 'E']
kh_variance_0hdf5_5Display.ScaleTransferFunction = 'PiecewiseFunction'
kh_variance_0hdf5_5Display.OpacityArray = ['POINTS', 'E']
kh_variance_0hdf5_5Display.OpacityTransferFunction = 'PiecewiseFunction'
kh_variance_0hdf5_5Display.DataAxesGrid = 'GridAxesRepresentation'
kh_variance_0hdf5_5Display.SelectionCellLabelFontFile = ''
kh_variance_0hdf5_5Display.SelectionPointLabelFontFile = ''
kh_variance_0hdf5_5Display.PolarAxes = 'PolarAxesRepresentation'
kh_variance_0hdf5_5Display.ScalarOpacityUnitDistance = 1.7320508075688774
kh_variance_0hdf5_5Display.Slice = 127

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
kh_variance_0hdf5_5Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_5Display.DataAxesGrid.XTitleFontFile = ''
kh_variance_0hdf5_5Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_5Display.DataAxesGrid.YTitleFontFile = ''
kh_variance_0hdf5_5Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_5Display.DataAxesGrid.ZTitleFontFile = ''
kh_variance_0hdf5_5Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_5Display.DataAxesGrid.XLabelFontFile = ''
kh_variance_0hdf5_5Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_5Display.DataAxesGrid.YLabelFontFile = ''
kh_variance_0hdf5_5Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_5Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
kh_variance_0hdf5_5Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_5Display.PolarAxes.PolarAxisTitleFontFile = ''
kh_variance_0hdf5_5Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_5Display.PolarAxes.PolarAxisLabelFontFile = ''
kh_variance_0hdf5_5Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_5Display.PolarAxes.LastRadialAxisTextFontFile = ''
kh_variance_0hdf5_5Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_5Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(kh_variance_0hdf5_5Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
kh_variance_0hdf5_5Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
kh_variance_0hdf5_5Display.SetScalarBarVisibility(renderView1, True)

# change representation type
kh_variance_0hdf5_5Display.SetRepresentationType('Volume')

# Rescale transfer function
rhoLUT.RescaleTransferFunction(0.0, 0.08)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(0.0, 0.08)

# current camera placement for renderView1
renderView1.CameraPosition = [543.5358867582901, 698.7981383075178, 605.5819902298207]
renderView1.CameraFocalPoint = [127.5, 127.5, 127.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 220.83647796503186

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/kh/stats/p0_1/kh_variance_256_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# create a new 'NetCDF Reader'
kh_variance_0hdf5_6 = NetCDFReader(FileName=['/scratch/snx3000/klye/3druns_new/kelvinhelmholtz_3d_tube/stats/p0_1/N128/kh_variance_0.hdf5'])
kh_variance_0hdf5_6.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# hide data in view
Hide(kh_variance_0hdf5_5, renderView1)

# show data in view
kh_variance_0hdf5_6Display = Show(kh_variance_0hdf5_6, renderView1)

# trace defaults for the display properties.
kh_variance_0hdf5_6Display.Representation = 'Outline'
kh_variance_0hdf5_6Display.ColorArrayName = [None, '']
kh_variance_0hdf5_6Display.OSPRayScaleArray = 'E'
kh_variance_0hdf5_6Display.OSPRayScaleFunction = 'PiecewiseFunction'
kh_variance_0hdf5_6Display.SelectOrientationVectors = 'E'
kh_variance_0hdf5_6Display.ScaleFactor = 12.700000000000001
kh_variance_0hdf5_6Display.SelectScaleArray = 'E'
kh_variance_0hdf5_6Display.GlyphType = 'Arrow'
kh_variance_0hdf5_6Display.GlyphTableIndexArray = 'E'
kh_variance_0hdf5_6Display.GaussianRadius = 0.635
kh_variance_0hdf5_6Display.SetScaleArray = ['POINTS', 'E']
kh_variance_0hdf5_6Display.ScaleTransferFunction = 'PiecewiseFunction'
kh_variance_0hdf5_6Display.OpacityArray = ['POINTS', 'E']
kh_variance_0hdf5_6Display.OpacityTransferFunction = 'PiecewiseFunction'
kh_variance_0hdf5_6Display.DataAxesGrid = 'GridAxesRepresentation'
kh_variance_0hdf5_6Display.SelectionCellLabelFontFile = ''
kh_variance_0hdf5_6Display.SelectionPointLabelFontFile = ''
kh_variance_0hdf5_6Display.PolarAxes = 'PolarAxesRepresentation'
kh_variance_0hdf5_6Display.ScalarOpacityUnitDistance = 1.732050807568877
kh_variance_0hdf5_6Display.Slice = 63

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
kh_variance_0hdf5_6Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_6Display.DataAxesGrid.XTitleFontFile = ''
kh_variance_0hdf5_6Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_6Display.DataAxesGrid.YTitleFontFile = ''
kh_variance_0hdf5_6Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_6Display.DataAxesGrid.ZTitleFontFile = ''
kh_variance_0hdf5_6Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_6Display.DataAxesGrid.XLabelFontFile = ''
kh_variance_0hdf5_6Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_6Display.DataAxesGrid.YLabelFontFile = ''
kh_variance_0hdf5_6Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_6Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
kh_variance_0hdf5_6Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_6Display.PolarAxes.PolarAxisTitleFontFile = ''
kh_variance_0hdf5_6Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_6Display.PolarAxes.PolarAxisLabelFontFile = ''
kh_variance_0hdf5_6Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_6Display.PolarAxes.LastRadialAxisTextFontFile = ''
kh_variance_0hdf5_6Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_6Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(kh_variance_0hdf5_6Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
kh_variance_0hdf5_6Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
kh_variance_0hdf5_6Display.SetScalarBarVisibility(renderView1, True)

# change representation type
kh_variance_0hdf5_6Display.SetRepresentationType('Volume')

# Rescale transfer function
rhoLUT.RescaleTransferFunction(0.0, 0.08)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(0.0, 0.08)

# current camera placement for renderView1
renderView1.CameraPosition = [270.7021867384425, 348.0288767257049, 301.60357944779304]
renderView1.CameraFocalPoint = [63.5, 63.5, 63.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 109.9852262806237

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/kh/stats/p0_1/kh_variance_128_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

# hide data in view
Hide(kh_variance_0hdf5_6, renderView1)

# create a new 'NetCDF Reader'
kh_variance_0hdf5_7 = NetCDFReader(FileName=['/scratch/snx3000/klye/3druns_new/kelvinhelmholtz_3d_tube/stats/p0_1/N64/kh_variance_0.hdf5'])
kh_variance_0hdf5_7.Dimensions = '(phony_dim_0, phony_dim_0, phony_dim_0)'

# show data in view
kh_variance_0hdf5_7Display = Show(kh_variance_0hdf5_7, renderView1)

# trace defaults for the display properties.
kh_variance_0hdf5_7Display.Representation = 'Outline'
kh_variance_0hdf5_7Display.ColorArrayName = [None, '']
kh_variance_0hdf5_7Display.OSPRayScaleArray = 'E'
kh_variance_0hdf5_7Display.OSPRayScaleFunction = 'PiecewiseFunction'
kh_variance_0hdf5_7Display.SelectOrientationVectors = 'E'
kh_variance_0hdf5_7Display.ScaleFactor = 6.300000000000001
kh_variance_0hdf5_7Display.SelectScaleArray = 'E'
kh_variance_0hdf5_7Display.GlyphType = 'Arrow'
kh_variance_0hdf5_7Display.GlyphTableIndexArray = 'E'
kh_variance_0hdf5_7Display.GaussianRadius = 0.315
kh_variance_0hdf5_7Display.SetScaleArray = ['POINTS', 'E']
kh_variance_0hdf5_7Display.ScaleTransferFunction = 'PiecewiseFunction'
kh_variance_0hdf5_7Display.OpacityArray = ['POINTS', 'E']
kh_variance_0hdf5_7Display.OpacityTransferFunction = 'PiecewiseFunction'
kh_variance_0hdf5_7Display.DataAxesGrid = 'GridAxesRepresentation'
kh_variance_0hdf5_7Display.SelectionCellLabelFontFile = ''
kh_variance_0hdf5_7Display.SelectionPointLabelFontFile = ''
kh_variance_0hdf5_7Display.PolarAxes = 'PolarAxesRepresentation'
kh_variance_0hdf5_7Display.ScalarOpacityUnitDistance = 1.7320508075688774
kh_variance_0hdf5_7Display.Slice = 31

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
kh_variance_0hdf5_7Display.DataAxesGrid.XTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_7Display.DataAxesGrid.XTitleFontFile = ''
kh_variance_0hdf5_7Display.DataAxesGrid.YTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_7Display.DataAxesGrid.YTitleFontFile = ''
kh_variance_0hdf5_7Display.DataAxesGrid.ZTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_7Display.DataAxesGrid.ZTitleFontFile = ''
kh_variance_0hdf5_7Display.DataAxesGrid.XLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_7Display.DataAxesGrid.XLabelFontFile = ''
kh_variance_0hdf5_7Display.DataAxesGrid.YLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_7Display.DataAxesGrid.YLabelFontFile = ''
kh_variance_0hdf5_7Display.DataAxesGrid.ZLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_7Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
kh_variance_0hdf5_7Display.PolarAxes.PolarAxisTitleColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_7Display.PolarAxes.PolarAxisTitleFontFile = ''
kh_variance_0hdf5_7Display.PolarAxes.PolarAxisLabelColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_7Display.PolarAxes.PolarAxisLabelFontFile = ''
kh_variance_0hdf5_7Display.PolarAxes.LastRadialAxisTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_7Display.PolarAxes.LastRadialAxisTextFontFile = ''
kh_variance_0hdf5_7Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0784313725490196, 0.0784313725490196, 0.0784313725490196]
kh_variance_0hdf5_7Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(kh_variance_0hdf5_7Display, ('POINTS', 'rho'))

# rescale color and/or opacity maps used to include current data range
kh_variance_0hdf5_7Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
kh_variance_0hdf5_7Display.SetScalarBarVisibility(renderView1, True)

# change representation type
kh_variance_0hdf5_7Display.SetRepresentationType('Volume')

# Rescale transfer function
rhoLUT.RescaleTransferFunction(0.0, 0.08)

# Rescale transfer function
rhoPWF.RescaleTransferFunction(0.0, 0.08)

# current camera placement for renderView1
renderView1.CameraPosition = [134.28533672851873, 172.6442459347985, 149.61437405677924]
renderView1.CameraFocalPoint = [31.5, 31.5, 31.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 54.559600438419636

# save screenshot
SaveScreenshot('/home/kjetil/projects/3druns/postprocessing/paraview_scripted_plots/kh/stats/p0_1/kh_variance_64_cm_0_0.png', renderView1, ImageResolution=[1107, 799], 
    # PNG options
    CompressionLevel='0')

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [134.28533672851873, 172.6442459347985, 149.61437405677924]
renderView1.CameraFocalPoint = [31.5, 31.5, 31.5]
renderView1.CameraViewUp = [-0.2110314943236713, 0.7131221018439862, -0.6685226819376691]
renderView1.CameraParallelScale = 54.559600438419636

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).