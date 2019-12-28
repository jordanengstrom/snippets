from pandas import (DataFrame
                    , options
                    )


# green = positive values, red = negative values
def color_negative_red(x):
    if isinstance(x, float):
        if x < 0:
            return 'color: red; font-weight: bold'
        else:
            return 'color: green; font-weight: bold'
    elif isinstance(x, object):
        return 'font-weight: bold'
    else:
        pass


# plain black with collapsed borders df
def style_df(*args):
    color = 'black'
    return 'color: %s' % color


def main():
    df = DataFrame()

    options.display.float_format = '{:,}'.format

    # email this dataframe as html
    html = (df.style.applymap(color_negative_red)
            .set_table_styles([{'selector': 'th, td',
                                'props': [('padding-top', '2px'),
                                          ('padding-bottom', '2px'),
                                          ('padding-right', '5px'),
                                          ('padding-left', '5px'),
                                          ('text-align', 'left'),
                                          ('border', '1px solid #ccc'),
                                          ],
                                },
                               {'selector': 'tbody',
                                'props': [('border-collapse', 'collapse')]
                                }])
            .format(formatter='{:,}', subset=df.select_dtypes(float).columns)
            .hidden_index()
            .render()
            )

    # or this one

    df2 = DataFrame()
    df2_floats = df2.select_dtypes(float).columns
    html2 = (df2.style.applymap(style_df)
                      .format(formatter='{:,.0f}', subset=df2_floats)
                      .set_table_styles([{'selector': 'th, td',
                                         'props': [('padding-top', '2px'),
                                                   ('padding-bottom', '2px'),
                                                    ('padding-right', '5px'),
                                                   ('padding-left', '5px'),
                                                    ('text-align', 'left'),
                                                    ('border', '1px solid #ccc'),
                                                    ],
                                          },
                                         {'selector': 'tbody',
                                          'props': [('border-collapse', 'collapse')]
                                          }
                                         ])
                      .hide_index()
                      .render()
             )


if __name__ == '__main__':
    main()
