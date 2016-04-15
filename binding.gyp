{
  'targets' : [
    {
      'target_name' : 'odbc_bindings',
      'sources' : [ 
        'src/odbc.cpp',
        'src/odbc_connection.cpp',
        'src/odbc_statement.cpp',
        'src/odbc_result.cpp',
        'src/dynodbc.cpp'
      ],
      'cflags' : ['-Wall', '-Wextra', '-Wno-unused-parameter'],
      'include_dirs': [
        "<!(node -e \"require('nan')\")",
	"C:/Program Files (x86)/Microsoft SQL Server/Client SDK/ODBC/110/SDK/Include/"
      ],
      'defines' : [
        'UNICODE'
      ],
      'conditions' : [
        [ 'OS == "linux"', {
          'libraries' : [ 
            '-lodbc' 
          ],
          'cflags' : [
            '-g'
          ]
        }],
        [ 'OS == "mac"', {
          'libraries' : [
            '-L/usr/local/lib',
            '-lodbc' 
          ]
        }],
        [ 'OS=="win"', {
          'sources' : [
            'src/strptime.c',
            'src/odbc.cpp'
          ],
          'libraries' : [ 
            '-lodbccp32.lib' 
          ]
        }]
      ]
    }
  ]
}
