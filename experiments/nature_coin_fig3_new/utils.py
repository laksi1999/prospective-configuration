import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import analysis_utils as au
import fit_data as fd


def fit_data_and_plot(df, kind='bar'):

    config_columns = [
        'init_std',
        'lr',
        'memory_lr',
    ]

    mean_columns = [
        'seed',
    ]

    metric_column = 'value'

    method_column = 'PC'

    plot_column = 'index'

    df = au.extract_plot(df, metric_column, plot_column)

    df, s = fd.fit_data(
        df=df,
        config_columns=config_columns,
        mean_columns=mean_columns,
        metric_column=metric_column,
        method_column=method_column,
        plot_column=plot_column,
        raw_data=[
            # first set of data
            [0.22080713446896594, 0.43893017632503795],
            [0.8531202468290524, 0.39274939657750035],
            [1.9123444859966976, 0.26056498546152623],
            [3.0424714105569675, 0.201139677683551],
            # end of first set of data
            [-0.11640312523021112, 0.3714387239076645],
            [0.14175337028257884, 0.3439451914701843],
            [-0.020462197801245807, 0.3411787647280591],
            [0.03718035941014053, 0.32706322827787343],
            [0.033150320453097404, 0.318307210303033],
            [-0.017251166761278913, 0.3075101725983352],
            [-0.19848591869721455, 0.31955002231688245],
            [0.15613150927125607, 0.28873279108364724],
            [-0.20298396217830117, 0.2865513699965767],
            [-0.15698951756533663, 0.2690636009481425],
            [-0.19645789909302458, 0.2246014378138989],
            [-0.24306334961237974, 0.21043910091130885],
            [0.12779123531527414, 0.22070660016380161],
            [0.10038697040738054, 0.20116567793488677],
            [0.09235289274462977, 0.18500045500439843],
            [-0.04258841168798, 0.19504088539522552],
            [0.12671222488484002, 0.16481385986731206],
            [0.07606373528277466, 0.14122209848028533],
            [0.049101474647588184, 0.1445769975776433],
            [-0.08973986748538554, 0.15259547508959254],
            [-0.26820559265406274, 0.10807091135214308],
            [0.21768710430867522, 0.07731261402193557],
            [0.12844124159866865, 0.05437692564361457],
            [-0.11992615928620642, -0.0110544401929219],
            [0.9212279052030836, 0.3207261003523035],
            [1.1061936932057006, 0.3019539188878827],
            [1.1213128393574467, 0.2851256895483324],
            [1.0054817196566233, 0.2850736890456609],
            [0.8545502606525193, 0.26682411263308886],
            [0.8503382199361256, 0.24864040352390082],
            [1.1671512824623957, 0.2595570423847431],
            [1.192761530028124, 0.18616786628937415],
            [1.0694033375655958, 0.19621349673046845],
            [0.8724514336971922, 0.19410487634713813],
            [0.8446311647679257, 0.1530149458111429],
            [0.8794845016835162, 0.15841779803871442],
            [1.0841584801986417, 0.16052988512222288],
            [0.8056567880156167, 0.13414223004155712],
            [0.8476731941742099, 0.11059206905666757],
            [1.0294409512625289, 0.126161886231567],
            [1.071756360311483, 0.11810007496739133],
            [1.0676873209774356, 0.10732383746376217],
            [0.9857085285157754, 0.0608223879497502],
            [0.8387941083430479, 0.05065542300242237],
            [1.135495976461106, 0.019812191517851407],
            [1.0117477802285424, 0.009655626671057793],
            [2.1941222098480284, 0.25665108096044936],
            [2.0967252683442594, 0.2114895110652737],
            [1.7872962771973468, 0.18306776965510674],
            [1.806549463311478, 0.18038281036716697],
            [2.01873751446264, 0.17172385999731338],
            [2.034051662499404, 0.16499672830170697],
            [2.214987411544979, 0.13746852886244576],
            [2.2105023681895584, 0.1051432830517362],
            [1.774803156430512, 0.1359241139331014],
            [1.7937443395286157, 0.11707739841485143],
            [1.836202749959916, 0.11642305875623465],
            [1.8786611603912164, 0.11576871909761799],
            [1.7393128133571962, 0.09752434273531319],
            [1.8240476324604464, 0.08678797228373208],
            [2.2679889238929314, 0.08294686848639538],
            [2.1363886517569672, 0.0660527718434612],
            [2.144045725775349, 0.06268920599565808],
            [2.2633088786524937, 0.04052052503174208],
            [2.2551968002357357, 0.020314863043676135],
            [2.2626978727461036, 0.00887041908071784],
            [2.270185945130802, -0.003247431391836808],
            [2.258407831275701, -0.013353729086047816],
            [2.184931121000836, -0.019447321324106204],
            [2.026927593633405, -0.004030038957043236],
            [1.8494758782668232, 0.003971105054015656],
            [3.187929816654894, 0.13588511355609778],
            [3.1029089947869495, 0.13180654079656112],
            [3.1104620677999884, 0.12305572287198785],
            [3.12935125039542, 0.10151538131535276],
            [3.1333552891011274, 0.10892458627100071],
            [2.944099459628109, 0.10547261956865589],
            [2.9472844904167403, 0.07045721441973946],
            [3.1673766179739737, 0.07122942188441161],
            [3.001508014577474, 0.07923576594573756],
            [3.005031048633471, 0.06172893004632385],
            [3.143638388504422, 0.04158913536164188],
            [3.1282852400906536, 0.046296047528459505],
            [2.8848188865825697, 0.03473893580971288],
            [2.888796925036942, 0.04080132774616829],
            [2.9195682224928166, 0.03475453596051431],
            [3.162306568963499, 0.008600883141870408],
            [3.0772337465928836, 0.0018286843439487832],
            [3.1542724913007487, -0.007564339788617924],
            [3.099775964500991, -0.030484428016137488],
            [2.940875428462475, -0.06153219481121641],
            [2.9332833550724327, -0.05480159641543203],
        ],
        process_plot_column_fn_in_raw_data=lambda plot: np.round(plot),
        fit_with='k',
    )

    plot_kwargs = {
        'data': df,
        'x': plot_column,
        'y': f'{metric_column}: fitted',
        'col': method_column,
        'palette': 'rocket',
        'aspect': 0.84,
        'sharey': True,
    }

    if kind == 'strip':

        g = au.nature_catplot(
            kind='strip',
            linewidth=1,
            alpha=0.5,
            **plot_kwargs,
        )

    elif kind == 'bar':

        g = au.nature_catplot(
            kind='bar',
            capsize=0.2,
            errwidth=3,
            **plot_kwargs,
        )

    # [ax.set_ylim(-0.1, 1.0) for ax in g.axes.flat]